from confluent_kafka import Producer, Consumer


# Kafka Consumer setup
consumer = Consumer(
    'weather',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    weather_data = message.value
    print(f"Received weather data: {json.dumps(weather_data, indent=2)}")