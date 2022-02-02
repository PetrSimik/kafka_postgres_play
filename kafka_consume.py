#This is simple example how to read data from Kafka hello world
#see more on https://github.com/confluentinc/confluent-kafka-python

from confluent_kafka import Consumer


conf = {
    'bootstrap.servers': 'kafka.host.cz:9093',
    'group.id': 'simik-test-2',
    'auto.offset.reset': 'earliest',
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

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()

