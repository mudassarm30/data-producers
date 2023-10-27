from producers.adapters.azure_event_hubs import AzureEventHubsAdapter
from producers.adapters.messaging_system import AbstractionLayer
from config import CONFIG_PARAMS, COMMON_DATA_FORMAT

# Example Usage
abstraction_layer_azure_event_hub = AbstractionLayer(AzureEventHubsAdapter())
abstraction_layer_azure_event_hub.connect("azure_event_hubs")
abstraction_layer_azure_event_hub.publish(
    "HandsOnTopic", {"timestamp": "2023-10-15 12:00:00", "data": "example_data"})
