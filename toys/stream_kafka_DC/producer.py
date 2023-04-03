import time

from kafka import KafkaProducer

from toys.code_data_stream.generate import generate_signal
from toys.stream_kafka_DC.config import KAFKA_BOOTSTRAP_SERVER, KAFKA_TOPIC

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)
    print(f"> Kafka connected: {producer.bootstrap_connected()}")

    while True:
        signal = generate_signal()
        print(f"> Sending signal {signal}...")

        signal_json_bytes = signal.to_json().encode("utf-8")
        producer.send(KAFKA_TOPIC, signal_json_bytes)

        time.sleep(2)
