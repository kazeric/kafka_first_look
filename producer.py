from kafka import KafkaProducer
import json
from faker import Faker
import time



fake = Faker()

fake.name()
fake.address()

def generate_user():
    return{
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email()
    }



producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    user = generate_user()
    producer.send('corhot4', user)
    print(f"Sent: {user}")
    producer.flush()
    time.sleep(5)