import json
import uuid
from consumers.adapters.messaging_system import MessagingSystem
from confluent_kafka import Consumer, KafkaError


class KafkaAdapter(MessagingSystem):

    def __init__(self):
        self.consumer = None

    def connect(self, connection_params):
        self.consumer = Consumer({
            'bootstrap.servers': connection_params['bootstrap_servers'],
            'group.id': 'consumer_group_1',
            'auto.offset.reset': 'earliest'
        })

    def consume(self, topic):
        self.consumer.subscribe([topic])
        try:
            while True:
                msg = self.consumer.poll(1.0)

                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        print(msg.error())
                        break

                print('Received message: {}'.format(
                    msg.value().decode('utf-8')))

        except KeyboardInterrupt:
            pass

        finally:
            self.consumer.close()
