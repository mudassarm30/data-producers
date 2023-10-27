from consumers.adapters.azure_event_hubs import AzureEventHubsAdapter
from consumers.adapters.messaging_system import AbstractionLayer
from config import CONFIG_PARAMS, COMMON_DATA_FORMAT

# Example Usage
abstraction_layer_azure_event_hub = AbstractionLayer(AzureEventHubsAdapter())
abstraction_layer_azure_event_hub.connect("azure_event_hubs")
abstraction_layer_azure_event_hub.consume("handson-eventhub")
