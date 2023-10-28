from consumers.adapters.google_pubsub import GoogleCloudPubSubAdapter
from consumers.adapters.kafka import KafkaAdapter
from consumers.adapters.messaging_system import AbstractionLayer
from config import CONFIG_PARAMS, COMMON_DATA_FORMAT

# Example Usage
abstraction_layer_consumer = AbstractionLayer(
    KafkaAdapter())
abstraction_layer_consumer.connect("kafka")
abstraction_layer_consumer.consume("HandsOnTopic")
