from adapters.kafka import KafkaAdapter
from adapters.messaging_system import AbstractionLayer
from config import CONFIG_PARAMS, COMMON_DATA_FORMAT

# Example Usage
abstraction_layer_kafka = AbstractionLayer(KafkaAdapter())
abstraction_layer_kafka.connect("kafka")
abstraction_layer_kafka.publish(
    "HandsOnTopic", {"timestamp": "2023-10-15 12:00:00", "data": "example_data"})
