#This is simple example how to write data to Kafka
from confluent_kafka import Producer


conf = {
    'bootstrap.servers': 'kafka.host.cz:9093',        
    'sasl.username': 'simik-test-1',
    'sasl.mechanisms': 'SCRAM-SHA-256',
    'security.protocol':'SASL_PLAINTEXT',
    'sasl.password': 'secret_password'
}


# test_data = ['testdata1','testdata2','testdata3','testdata4','testdata5','testdata6','testdata7',]
test_data = ['{"data":"value1","date":"2020.01.02"}','{"data":"value2","date":"2020.01.02"}','{"data":"value3","date":"2020.01.02"}','{"data":"value4","date":"2020.01.02"}']

p = Producer(conf)

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

for data in test_data:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('simik-test-1', data.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()

