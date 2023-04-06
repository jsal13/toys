import json
from abc import ABC, abstractmethod
from typing import Any, Type

import pandas as pd
import psycopg
from kafka import KafkaConsumer

from toys.stream_kafka_DC.config import KAFKA_BOOTSTRAP_SERVER, KAFKA_TOPIC


# TODO: Why can't I just do this with functions?  Abstract functions or somesuch nonsense.
class MessageProcessor(ABC):
    """Processor for messages consumed by the consumer."""

    @abstractmethod
    def processor(self, msg: dict[str, Any]) -> Any:
        """Process ``msg``."""


class PrintMessageProcessor(MessageProcessor):
    """Processor for messages which ``print``s to terminal."""

    def processor(self, msg: dict[str, Any]) -> Any:
        """Print ``msg`` to terminal."""
        print(msg)


class BatchMessageProcessor(MessageProcessor):
    """Processor for messages which ``print``s to terminal in batches."""

    def __init__(self) -> None:
        self.batch_container: list[dict[str, Any]] = []
        self.batch_number = 1
        self.batch_size = 5

    def processor(self, msg: dict[str, Any]) -> Any:
        """Print ``msg`` to terminal."""
        if len(self.batch_container) < self.batch_size:
            self.batch_container.append(msg)
        else:
            print(
                f"> Batch number {self.batch_number}...",
                self.batch_container,
                sep="\n",
                end="\n\n",
            )
            self.batch_number += 1
            self.batch_container.clear()


class BatchToPostgresMessageProcessor(MessageProcessor):
    """Processor for messages which INSERTS to a PG table."""

    def __init__(self) -> None:
        self.batch_container: list[dict[str, Any]] = []
        self.batch_number = 1
        self.batch_size = 5

        self.conn = self._connect()

    def _connect(self) -> psycopg.Connection[tuple[Any, ...]]:
        """Connect to the PostgreSQL database server."""
        conn = None
        print("Connecting to the PostgreSQL database...")
        conn = psycopg.connect(
            host="db",  # ``localhost``, if not docker-composed.
            dbname="postgres",
            user="postgres",
            password="example",
            autocommit=True,
        )
        print("Connection successful")
        return conn

    def _insert_signal_to_events_table(self, signals: list[dict[str, Any]]) -> None:
        """Insert a series of signals into the ``events`` table."""
        # NOTE: This is vulnerable to SQL Injections.  Do not do this.
        # This is an example for toy purposes.

        columns = [
            "sensor_id",
            "dt",
            "value_1",
            "value_2",
            "value_3",
            "heat_index",
            "power",
        ]
        df_signals = pd.DataFrame(signals, columns=columns)
        print(df_signals)

        values_str = ",".join(
            [str(row) for row in df_signals.itertuples(index=False, name=None)]
        )

        sql = f"INSERT INTO events ({','.join(columns)}) values {values_str};"

        with self.conn.cursor() as cur:
            cur.execute(sql)

    def processor(self, msg: dict[str, Any]) -> Any:
        """Print ``msg`` to terminal."""
        if len(self.batch_container) < self.batch_size:
            self.batch_container.append(msg)
        else:
            print(f"> Batch number {self.batch_number}...")
            self._insert_signal_to_events_table(self.batch_container)
            print()
            self.batch_number += 1
            self.batch_container.clear()


def initialize_consumer(
    message_processor: Type[MessageProcessor] = PrintMessageProcessor,
) -> Any:
    """Initialize Kafka topic consumer."""
    # TODO: Use poll method to poll Kafka.
    # Kafka-types?  What the heck.
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
    )
    print(f"> Kafka connected: {consumer.bootstrap_connected()}")
    processor = message_processor()

    for msg in consumer:
        record = json.loads(msg.value)
        processor.processor(record)


if __name__ == "__main__":
    # Pick the message_processor appropriate to your task.

    # initialize_consumer(message_processor=PrintMessageProcessor)
    # initialize_consumer(message_processor=BatchMessageProcessor)
    initialize_consumer(message_processor=BatchToPostgresMessageProcessor)
