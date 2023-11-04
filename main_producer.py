from producers.adapters.amazon_kinesis_stream import AmazonKinesisDataStreamAdapter
from producers.adapters.google_pubsub import GoogleCloudPubSubAdapter
from producers.adapters.kafka import KafkaAdapter
from producers.adapters.messaging_system import AbstractionLayer
from config import CONFIG_PARAMS, COMMON_DATA_FORMAT

# Example Usage
abstraction_layer_publisher = AbstractionLayer(
    AmazonKinesisDataStreamAdapter())
abstraction_layer_publisher.connect("kinesis_data_stream")
abstraction_layer_publisher.publish(
    "HandsOnKinesisDataStream", {"timestamp": "2023-10-15 12:00:00", "data": "example_data"})
