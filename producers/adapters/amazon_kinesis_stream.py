import json
import uuid
import boto3
from producers.adapters.messaging_system import MessagingSystem


class AmazonKinesisDataStreamAdapter(MessagingSystem):

    def connect(self, connection_params):
        self.kinesis_client = boto3.client('kinesis',
                                           region_name=connection_params['region'],
                                           aws_access_key_id=connection_params['access_key'],
                                           aws_secret_access_key=connection_params['secret_key'])

    def publish(self, stream_name, data):
        partition_key = str(uuid.uuid4())
        self.kinesis_client.put_record(StreamName=stream_name,
                                       Data=json.dumps(data),
                                       PartitionKey=partition_key)
