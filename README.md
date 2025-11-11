# Kafka Introduction Project

A hands-on introduction to Apache Kafka featuring two separate implementations:

1. **Local Kafka Setup**: Basic producer/consumer with fake data generation
2. **Confluent Cloud**: Weather data streaming using the OpenWeatherMap API

## Project Overview

This project demonstrates core Kafka concepts including message production, consumption, serialization, and real-time data streaming. It includes examples of both self-managed local Kafka and Confluent Cloud managed services.

## Project Structure

### Local Kafka Implementation

#### `producer.py`

A simple Kafka producer that generates fake user data using the Faker library and sends it to a local Kafka broker.

**Features:**

- Generates synthetic user profiles (name, address, email)
- Sends messages to the `corhot4` topic
- Publishes messages every 5 seconds
- Uses JSON serialization

**Requirements:**

- kafka-python
- faker
- Local Kafka broker running on `localhost:9092`

**Usage:**

```bash
python producer.py
```

#### `consumer.py`

A simple Kafka consumer that listens to the `corhot4` topic on a local Kafka broker and prints incoming messages.

**Features:**

- Consumes messages from the `corhot4` topic
- Deserializes JSON messages
- Starts from the latest message offset

**Requirements:**

- kafka-python

**Usage:**

```bash
python consumer.py
```

### Confluent Cloud Implementation

#### `we_con_producer.py`

A producer that fetches real-time weather data from the OpenWeatherMap API and streams it to Confluent Cloud.

**Features:**

- Fetches weather data from OpenWeatherMap API
- Streams weather information for a specified city (Nairobi)
- Secure connection to Confluent Cloud using SASL_SSL
- Environment variable configuration for sensitive credentials
- Produces to a configurable Kafka topic

**Requirements:**

- confluent-kafka
- requests
- python-dotenv
- OpenWeatherMap API key
- Confluent Cloud account and credentials

**Environment Variables:**
Create a `.env` file with the following:

```
OPEN_WEATHER_API_KEY=your_openweather_api_key
KAFKA_BOOTSTRAP_SERVERS=your_confluent_bootstrap_server
CONFLUENT_API_KEY=your_confluent_api_key
CONFLUENT_API_SECRET=your_confluent_api_secret
KAFKA_TOPIC=your_topic_name
KAFKA_CLIENT_ID=your_client_id
```

**Usage:**

```bash
python we_con_producer.py
```

#### `we_con_consumer.py`

A consumer that reads weather data from Confluent Cloud and processes the streamed messages.

**Features:**

- Consumes weather data from the `weather` topic
- Deserializes JSON weather data
- Pretty-prints incoming weather information
- Supports both local and Confluent Cloud brokers

**Requirements:**

- confluent-kafka

**Usage:**

```bash
python we_con_consumer.py
```

## Getting Started

### Prerequisites

- Python 3.7+
- Apache Kafka (for local setup) or Confluent Cloud account
- OpenWeatherMap API key (for weather streaming)

### Installation

1. **Clone the repository:**

```bash
git clone <repository-url>
cd kafka_intro
```

2. **Install dependencies:**

```bash
pip install kafka-python faker confluent-kafka requests python-dotenv
```

3. **For Local Kafka Setup:**

   - Install and start Apache Kafka
   - Ensure broker is running on `localhost:9092`
   - Create necessary topics (`corhot4`, `weather`)

4. **For Confluent Cloud Setup:**
   - Sign up for a Confluent Cloud account
   - Create a Kafka cluster
   - Generate API credentials
   - Create a `.env` file with your credentials
   - Obtain an OpenWeatherMap API key from [openweathermap.org](https://openweathermap.org/api)

## Running the Project

### Local Kafka Example

Terminal 1 - Start Producer:

```bash
python producer.py
```

Terminal 2 - Start Consumer:

```bash
python consumer.py
```

### Confluent Cloud Example

Terminal 1 - Start Weather Producer:

```bash
python we_con_producer.py
```

Terminal 2 - Start Weather Consumer:

```bash
python we_con_consumer.py
```

## Learning Objectives

This project demonstrates:

- **Producer/Consumer Pattern**: Basic message production and consumption
- **Data Serialization**: JSON encoding/decoding of Kafka messages
- **Kafka Topics**: Publishing and subscribing to different topics
- **Real-time Streaming**: Processing continuous data streams
- **Cloud Integration**: Working with managed Kafka services (Confluent Cloud)
- **Secure Authentication**: SASL_SSL configuration for cloud-based brokers
- **API Integration**: Fetching and streaming real-world API data

## Technologies Used

- **Apache Kafka**: Distributed event streaming platform
- **Confluent Cloud**: Managed Kafka service
- **Faker**: Generates fake user data
- **OpenWeatherMap API**: Real-time weather data
- **python-dotenv**: Environment variable management

## Next Steps

Consider extending this project with:

- Error handling and retry logic
- Data transformations and filtering
- Avro schema integration
- Stream processing with Kafka Streams
- Consumer groups for parallel processing
- Monitoring and logging

## Resources

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Confluent Cloud Documentation](https://docs.confluent.io/cloud/current/overview.html)
- [kafka-python Library](https://kafka-python.readthedocs.io/)
- [Confluent Kafka Python Client](https://docs.confluent.io/kafka-clients/python/current/overview.html)
- [OpenWeatherMap API](https://openweathermap.org/api)
