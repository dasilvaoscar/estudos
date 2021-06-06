from kafka import KafkaConsumer

consumer = KafkaConsumer('teste')

for message in consumer:
  print(message)