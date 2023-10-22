# Configuration parameters for each messaging system
CONFIG_PARAMS = {
    "kafka": {"bootstrap_servers": "localhost:9092"},
    "amazon_msk": {"bootstrap_servers": "my-cluster:9092"},
    "azure_event_hubs": {"connection_string": "Endpoint=sb://mynamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=mykey"},
    "google_cloud_pubsub": {"project_id": "my-project", "credentials_path": "/path/to/credentials.json"}
}

COMMON_DATA_FORMAT = {
    "timestamp": "",
    "data": ""
}
