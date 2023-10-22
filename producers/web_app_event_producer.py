class WebAppEventProducer:
    def __init__(self, adapter, topic):
        self.adapter = adapter
        self.topic = topic

    def send_event_data(self, event):
        self.adapter.send_to_messaging_system(self.topic, event)
