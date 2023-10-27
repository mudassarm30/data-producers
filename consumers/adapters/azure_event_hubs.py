import json
import uuid
from azure.eventhub import EventHubConsumerClient
from consumers.adapters.messaging_system import MessagingSystem


class AzureEventHubsAdapter(MessagingSystem):

    def __init__(self):
        self.client = None

    def connect(self, connection_params):
        self.client = EventHubConsumerClient.from_connection_string(
            conn_str=connection_params.get("connection_string"),
            consumer_group=connection_params.get("consumer_group"),
            eventhub_name=connection_params.get("event_hub_name")
        )

    def consume(self, topic):
        with self.client:
            self.client.receive(on_event=self.on_event, on_error=self.on_error)

    def on_event(self, partition_context, event):
        # Process the received event
        print("Received event from partition: {}".format(
            partition_context.partition_id))
        print("  Event data: {}".format(event.body_as_str(encoding='UTF-8')))
        print("  Enqueued time: {}".format(event.enqueued_time))
        print("  Sequence number: {}".format(event.sequence_number))
        print("  Offset: {}".format(event.offset))
        print("")

    def on_error(self, partition_context, error):
        # Handle errors during event processing
        print("An error occurred on partition: {}".format(
            partition_context.partition_id))
        print("  Error: {}".format(error))
        print("")
