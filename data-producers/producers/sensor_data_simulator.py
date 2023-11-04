import random
import time


class SensorDataSimulator:
    def __init__(self, adapter, topic):
        self.adapter = adapter
        self.topic = topic

    def send_sensor_data(self):
        while True:
            temperature = random.randint(0, 100)
            humidity = random.randint(0, 100)
            data = f"{{'temperature': {temperature}, 'humidity': {humidity}}}"
            self.adapter.send_to_messaging_system(self.topic, data)
            time.sleep(1)
