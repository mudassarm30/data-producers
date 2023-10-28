import json
import uuid
from producers.adapters.messaging_system import MessagingSystem
from google.cloud import pubsub
from google.oauth2.service_account import Credentials


class GoogleCloudPubSubAdapter(MessagingSystem):

    def connect(self, connection_params):

        self.project_id = connection_params['project_id']

        credentials = Credentials.from_service_account_file(
            connection_params['credentials_path'])
        self.publisher = pubsub.PublisherClient(credentials=credentials)

    def publish(self, topic, data):

        self.topic_path = self.publisher.topic_path(
            self.project_id, topic)
        data = json.dumps(data).encode('utf-8')
        future = self.publisher.publish(self.topic_path, data=data)
        future.result()
