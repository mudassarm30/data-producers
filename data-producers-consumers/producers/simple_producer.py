class SimpleProducer:
    def __init__(self, adapter, topic):
        self.adapter = adapter
        self.topic = topic

    def send_data(self, data):
        self.adapter.send_to_messaging_system(self.topic, data)
