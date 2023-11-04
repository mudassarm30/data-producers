import json
import boto3
from consumers.adapters.messaging_system import MessagingSystem


class AmazonKinesisDataStreamAdapter(MessagingSystem):

    def __init__(self):
        pass

    def connect(self, connection_params):
        self.kinesis_client = boto3.client('kinesis',
                                           region_name=connection_params['region'],
                                           aws_access_key_id=connection_params['access_key'],
                                           aws_secret_access_key=connection_params['secret_key'])

    def consume(self, stream_name):
        shard_iterator = self.kinesis_client.get_shard_iterator(StreamName=stream_name,
                                                                ShardId='shardId-000000000000',
                                                                ShardIteratorType='TRIM_HORIZON')['ShardIterator']

        while True:
            records = self.kinesis_client.get_records(
                ShardIterator=shard_iterator, Limit=100)
            for record in records['Records']:
                print(record['Data'].decode())
            shard_iterator = records['NextShardIterator']
