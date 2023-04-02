import json
import random
import time
from datetime import datetime, timedelta
from enum import Enum, auto

import numpy as np
from config import KAFKA_BOOTSTRAP_SERVER, KAFKA_TOPIC
from kafka import KafkaProducer
from pydantic import Field
from pydantic.dataclasses import dataclass

# NOTE: This is replicated from ``/toys/code_data_stream/``.
# TODO: Make this DRY.


class Power(Enum):
    """Enum for ``Power`` field in ``Signal``."""

    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()


@dataclass
class Signal:
    """
    Single ``Signal`` for use in a data stream.

    Note: We cannot constrain the datetime to a certain type because of the following:
    https://github.com/pydantic/pydantic/issues/156
    """

    value_1: int
    value_2: float
    power: Power
    dt: str = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def to_json(self) -> str:
        """Convert dataclass values to json."""
        # Remove "__pydantic_initialized__" from the dict.
        values = self.__dict__.copy()
        del values["__pydantic_initialised__"]

        return json.dumps(values, default=lambda x: x.name)


def generate_signal() -> Signal:
    """Generate a single signal."""
    value_1 = random.randint(0, 100)
    value_2 = round(np.random.normal(), 4)
    power = random.choice([Power.LOW, Power.MEDIUM, Power.HIGH])
    dt = (datetime.now() + timedelta(seconds=random.randint(-10, 10))).strftime(
        ("%Y-%m-%d %H:%M:%S")
    )

    return Signal(value_1=value_1, value_2=value_2, power=power, dt=dt)


if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)

    while True:
        signal = generate_signal()
        print(f"> Sending signal {signal}...")

        signal_json_bytes = signal.to_json().encode("utf-8")
        producer.send(KAFKA_TOPIC, signal_json_bytes)

        time.sleep(2)
