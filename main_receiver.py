from consumers.adapters.amazon_kinesis_stream import AmazonKinesisDataStreamAdapter
from consumers.adapters.google_pubsub import GoogleCloudPubSubAdapter
from consumers.adapters.kafka import KafkaAdapter
from consumers.adapters.messaging_system import AbstractionLayer
from config import CONFIG_PARAMS, COMMON_DATA_FORMAT

# Example Usage
abstraction_layer_consumer = AbstractionLayer(
    AmazonKinesisDataStreamAdapter())
abstraction_layer_consumer.connect("kinesis_data_stream")
abstraction_layer_consumer.consume("HandsOnKinesisDataStream")
