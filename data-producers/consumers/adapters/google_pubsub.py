import json
import uuid
from consumers.adapters.messaging_system import MessagingSystem
from google.cloud import pubsub
from google.oauth2.service_account import Credentials


class GoogleCloudPubSubAdapter(MessagingSystem):

    def __init__(self):
        self.subscriber = None

    def connect(self, connection_params):

        self.project_id = connection_params['project_id']

        credentials = Credentials.from_service_account_file(
            connection_params['credentials_path'])
        self.subscriber = pubsub.SubscriberClient(credentials=credentials)

    def consume(self, topic):

        subscription_path = self.subscriber.subscription_path(
            self.project_id, f"{topic}-Subscription"
        )

        def callback(message):
            print(f"Received message: {message.data.decode('utf-8')}")
            message.ack()

        streaming_pull_future = self.subscriber.subscribe(
            subscription_path, callback=callback)
        try:
            streaming_pull_future.result()
        except Exception as ex:
            streaming_pull_future.cancel()
            raise
