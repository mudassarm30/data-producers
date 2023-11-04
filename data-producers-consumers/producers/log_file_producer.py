class LogFileProducer:
    def __init__(self, adapter, topic, log_file_path):
        self.adapter = adapter
        self.topic = topic
        self.log_file_path = log_file_path

    def send_log_data(self):
        with open(self.log_file_path, 'r') as file:
            for line in file:
                self.adapter.send_to_messaging_system(self.topic, line)
