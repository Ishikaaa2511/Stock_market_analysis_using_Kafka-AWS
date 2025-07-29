# STOCK MARKET REAL-TIME ANALYSIS USING KAFKA & AWS

In this project we tried to make an end-to-end data engineering project 

Architecture:
-


<img width="827" height="645" alt="Stock_market_kafka_architecture" src="https://github.com/user-attachments/assets/0c603256-9532-4020-b00a-31909abd5a9e" />

Technologies used:
-
1. Python
2. AWS - S3, Athena, Glue Crawler, Glue catalogue, EC2
3. Apache Kafka


Flow:
-
1. Deploy an EC2 instance.
    <img width="1887" height="515" alt="ec2" src="https://github.com/user-attachments/assets/f93e343e-8cd0-4055-9f86-a7b383f8e97f" />
2. Download and set up the latest Kafka version in the environment of the deployed instance.
3. Configure Kafka to run over the public ip of our ec2 instance.
    <img width="1072" height="373" alt="Kafka" src="https://github.com/user-attachments/assets/6483c9e1-a1f1-440b-95b2-adfa8b25f594" />
4. Make topic to access the real-time streaming data.
    <img width="1085" height="233" alt="topic" src="https://github.com/user-attachments/assets/808885ee-f56f-4f34-9f8b-f2693d7b7cc4" />
5. Make a python application in our local env.
6. Write code to make a kafka producer in python.
7. Write code to make a kafka consumer in python.
    <img width="1831" height="611" alt="producer_consumer" src="https://github.com/user-attachments/assets/6ff9198a-9604-46df-9b05-90643e6366a9" />
8. In the producer we fetch the data from API, but for this case to simulate a real-time API, we use pandas to fetch dataset and make sample batches and then send it to kafka
9. In the consumer we fetch the data coming from the producer, and then dumps the data into s3 bucket in json format.
10. Run both producer and consumer, and the data from the consumer is seen in s3 bucket as different data objects.
    <img width="1874" height="497" alt="s3bucket" src="https://github.com/user-attachments/assets/14473f3b-8247-4b15-b9c4-0137c009f836" />
11. Set up a Glue crawler over the bucket.
12. The Glue crawler examines the data in real-time and saves in a Glue data catalogue, to be used by different AWS services
    <img width="1899" height="734" alt="AWS_GLUE" src="https://github.com/user-attachments/assets/d1feb6c7-1994-42b6-87c1-00b2ac94e653" />
    
13. Open AWS Athena and connect it to our catalogue
14. Using Athena we can run all kinds of analytical queries on this data.
    <img width="1854" height="851" alt="AWS_ATHENA" src="https://github.com/user-attachments/assets/46779ae8-187d-4d2c-b820-2688a22b98d4" />

Final Output Analytics(Athena):
-
   <img width="1897" height="817" alt="FINAL" src="https://github.com/user-attachments/assets/38ebe95e-f7f1-4a06-aef8-521ef7036792" />

