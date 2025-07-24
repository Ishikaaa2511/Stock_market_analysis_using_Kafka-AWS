import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json
import constants  # Make sure constants.py is in same folder

# Access constants correctly
S3_FILE_PATH = f's3://{constants.S3_BUCKET}/{constants.S3_STORAGE_FILENAME}'

# Set up Kafka producer
producer = KafkaProducer(
    bootstrap_servers=[constants.BOOTSTRAP_SERVER],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# Read stock data
df = pd.read_csv('indexProcessed.csv')
df.head()

# Produce stock data to Kafka topic
while True:
    dict_stock = df.sample(1).to_dict(orient='records')[0]
    producer.send(constants.KAFKA_TOPIC_NAME, value=dict_stock)
    print(f"Sent: {dict_stock}")
    sleep(1)
