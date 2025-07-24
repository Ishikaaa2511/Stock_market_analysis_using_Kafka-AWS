import pandas as pd
from kafka import KafkaConsumer
from time import sleep
from json import dumps, loads
import constants
import json
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    constants.KAFKA_TOPIC_NAME,
    bootstrap_servers=[constants.BOOTSTRAP_SERVER],
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

s3 = S3FileSystem(
    key='your-key',
    secret='your-secret-key',
    client_kwargs={'region_name': 'ap-south-1'}
)

for count, i in enumerate(consumer):
    print(count)
    print(i.value)

    s3_path = f"s3://{constants.S3_BUCKET}/{constants.S3_STORAGE_FILENAME}_{count}.json"
    with s3.open(s3_path, 'w') as file:
        json.dump(i.value, file)
