# Producer
from kafka import KafkaProducer

def producer():
  producer = KafkaProducer(bootstrap_servers='localhost:9092')
  producer.send('teste', key=b'test', value=b'test')
  
producer()

