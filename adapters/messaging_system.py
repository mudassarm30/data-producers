from abc import ABC, abstractmethod

from config import COMMON_DATA_FORMAT, CONFIG_PARAMS


class MessagingSystem(ABC):
    @abstractmethod
    def connect(self, connection_params):
        pass

    @abstractmethod
    def publish(self, topic, data):
        pass


class AbstractionLayer(MessagingSystem):
    def __init__(self, messaging_system):
        self.messaging_system = messaging_system

    def connect(self, system_name):
        connection_params = CONFIG_PARAMS[system_name]
        return self.messaging_system.connect(connection_params)

    def publish(self, topic, data):
        standardized_data = self._standardize_data(data)
        return self.messaging_system.publish(topic, standardized_data)

    def _standardize_data(self, data):
        standardized_data = dict(COMMON_DATA_FORMAT)
        standardized_data["timestamp"] = data["timestamp"]
        standardized_data["data"] = data["data"]
        return standardized_data
