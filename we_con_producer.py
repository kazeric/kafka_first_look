import json
import requests
from confluent_kafka import Producer
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("OPEN_WEATHER_API_KEY")  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
TOPIC = os.getenv("KAFKA_TOPIC")

producer_conf = {
    'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVERS"),  # Replace with your Kafka bootstrap server
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': os.getenv("CONFLUENT_API_KEY"),  #
    'sasl.password': os.getenv("CONFLUENT_API_SECRET"),  # Replace with your Confluent Cloud API key and secret
    'client.id': os.getenv("KAFKA_CLIENT_ID")  # Replace with your client ID
}


# Kafka Producer setup
producer = Producer(producer_conf)


# OpenWeatherMap API setup
CITY = 'Nairobi'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def fetch_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

while True:
    weather_data = fetch_weather()
    if weather_data:
        producer.produce(TOPIC, json.dumps(weather_data).encode('utf-8'))
        producer.flush()
        print(f"Sent weather data for {CITY}")
    sleep(5)  