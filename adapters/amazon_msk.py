import json
import uuid
from adapters.messaging_system import MessagingSystem
from confluent_kafka import Producer


class AmazonMSKAdapter(MessagingSystem):

    def connect(self, connection_params):

        self.producer = Producer(
            {'bootstrap.servers': connection_params['bootstrap_servers']})

    def publish(self, topic, data):

        # create unique key string from UUID
        key = str(uuid.uuid4())
        data_str = json.dumps(data)

        self.producer.produce(topic, key=key, value=data_str.encode('utf-8'),
                              callback=self.delivery_report)

        # Wait for messages to be delivered
        self.producer.flush()

    def delivery_report(self, err, msg):
        if err is not None:
            print(f'Error: {err}')
        else:
            print(
                f'Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')
