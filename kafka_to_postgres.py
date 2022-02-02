#This is simple example how to read data from Kafka hello world
#see more on https://github.com/confluentinc/confluent-kafka-python

from confluent_kafka import Consumer
import json
import psycopg



conf = {
    'bootstrap.servers': 'kafka.host.cz:9093',
    'group.id': 'simik-test-7',
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
    field1 = data.get('data')
    field2 = data.get('date')
    with psycopg.connect("hostaddr=127.0.0.1 dbname=postgres user=postgres password=postgres") as conn:
    # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO test (data, date) VALUES ('{field1}','{field2}')")
            # Make the changes to the database persistent
            conn.commit()
    


c.close()

