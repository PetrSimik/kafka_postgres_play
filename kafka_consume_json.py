#This is simple example how to read data from Kafka hello world
#see more on https://github.com/confluentinc/confluent-kafka-python

from confluent_kafka import Consumer
import json


conf = {
    'bootstrap.servers': 'ntw-kafka.cz:9093',
    'group.id': 'simik-test-5',
    'auto.offset.reset': 'latest',
    'sasl.username': 'simik-test-1',
    'sasl.mechanisms': 'SCRAM-SHA-256',
    'security.protocol':'SASL_PLAINTEXT',
    'sasl.password': 'secret_password'
}



c = Consumer(conf)

c.subscribe(['simik-test-1'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    
    data = json.loads(msg.value().decode('utf-8'))
    print(f'Received message: {data}')
    


c.close()

