from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('weather', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')), auto_offset_reset='latest')

for msg in consumer:
    print (msg.value)