import json
import uuid
from azure.eventhub import EventHubProducerClient, EventData
from producers.adapters.messaging_system import MessagingSystem


class AzureEventHubsAdapter(MessagingSystem):

    def __init__(self):
        self.client = None

    def connect(self, connection_params):
        connection_str = connection_params.get("connection_string")
        self.client = EventHubProducerClient.from_connection_string(
            connection_str)

    def publish(self, topic, data):
        event_data_batch = self.client.create_batch()
        event_data = EventData(json.dumps(data))
        event_data_batch.add(event_data)
        self.client.send_batch(event_data_batch)
