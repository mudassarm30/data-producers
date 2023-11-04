# Configuration parameters for each messaging system
# Use proper key managers for respective cloud for storing credentials
CONFIG_PARAMS = {
    "kafka": {"bootstrap_servers": "localhost:9092"},
    "amazon_msk": {"bootstrap_servers": "b-1-public.kafkaclusterhandson.hf7jkq.c11.kafka.us-east-1.amazonaws.com:9198"},
    "azure_event_hubs": {"connection_string": "Endpoint=sb://handson-namespace.servicebus.windows.net/;SharedAccessKeyName=HandsOnPolicy;SharedAccessKey=8CXmCKCVM0Uj9yQQzuEVWwQJGR8l0ovHz+AEhO4tWa8=;EntityPath=handson-eventhub", "consumer_group": "$Default", "event_hub_name": "handson-eventhub"},
    "google_cloud_pubsub": {"project_id": "spheric-rhythm-403400", "credentials_path": "C:\\Users\\MudassarMa\\Downloads\\DataScience\\hands-on\\creds\\spheric-rhythm-403400-4303cc11c9b0.json"},
    "kinesis_data_stream": {"region": "us-east-1", "access_key": "your key here", "secret_key": "secret here"}
}

COMMON_DATA_FORMAT = {
    "timestamp": "",
    "data": ""
}
