from producers.adapters.google_pubsub import GoogleCloudPubSubAdapter
from producers.adapters.messaging_system import AbstractionLayer
from config import CONFIG_PARAMS, COMMON_DATA_FORMAT

# Example Usage
abstraction_layer_google_cloud_pubsub = AbstractionLayer(
    GoogleCloudPubSubAdapter())
abstraction_layer_google_cloud_pubsub.connect("google_cloud_pubsub")
abstraction_layer_google_cloud_pubsub.publish(
    "HandsOnTopic", {"timestamp": "2023-10-15 12:00:00", "data": "example_data"})
