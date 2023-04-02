from config import KAFKA_BOOTSTRAP_SERVER, KAFKA_TOPIC
from kafka import KafkaConsumer

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)
for msg in consumer:
    print(msg)
