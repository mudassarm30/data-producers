# Configuration parameters for each messaging system
CONFIG_PARAMS = {
    "kafka": {"bootstrap_servers": "localhost:9092"},
    "amazon_msk": {"bootstrap_servers": "b-1-public.kafkaclusterhandson.hf7jkq.c11.kafka.us-east-1.amazonaws.com:9198"},
    "azure_event_hubs": {"connection_string": "Endpoint=sb://handson-namespace.servicebus.windows.net/;SharedAccessKeyName=HandsOnPolicy;SharedAccessKey=8CXmCKCVM0Uj9yQQzuEVWwQJGR8l0ovHz+AEhO4tWa8=;EntityPath=handson-eventhub", "consumer_group": "$Default", "event_hub_name": "handson-eventhub"},
    "google_cloud_pubsub": {"project_id": "my-project", "credentials_path": "/path/to/credentials.json"}
}

COMMON_DATA_FORMAT = {
    "timestamp": "",
    "data": ""
}
