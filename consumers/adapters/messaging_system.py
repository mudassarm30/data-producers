# import libraries
from config import COMMON_DATA_FORMAT, CONFIG_PARAMS
from abc import ABC, abstractmethod
import requests
import json

# import model
from config import CONFIG_PARAMS

# set up connection
connection_params = []


class MessagingSystem(ABC):
    @abstractmethod
    def connect(self, connection_params):
        pass

    def consume(self, topic):
        pass


class AbstractionLayer(MessagingSystem):
    def __init__(self, messaging_system):
        self.messaging_system = messaging_system

    def connect(self, system_name):
        connection_params = CONFIG_PARAMS[system_name]
        return self.messaging_system.connect(connection_params)

    def consume(self, topic):
        data = self.messaging_system.consume(topic)
        return self._standardize_data(data)

    def _standardize_data(self, data):
        standardized_data = dict(COMMON_DATA_FORMAT)
        standardized_data["timestamp"] = data["timestamp"]
        standardized_data["data"] = data["data"]
        return standardized_data
