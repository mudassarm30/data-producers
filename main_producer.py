from producers.adapters.google_pubsub import GoogleCloudPubSubAdapter
from producers.adapters.kafka import KafkaAdapter
from producers.adapters.messaging_system import AbstractionLayer
from config import CONFIG_PARAMS, COMMON_DATA_FORMAT

# Example Usage
abstraction_layer_publisher = AbstractionLayer(
    KafkaAdapter())
abstraction_layer_publisher.connect("kafka")
abstraction_layer_publisher.publish(
    "HandsOnTopic", {"timestamp": "2023-10-15 12:00:00", "data": "example_data"})
