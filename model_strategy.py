from abc import ABC, abstractmethod

class ModelStrategy(ABC):
    @abstractmethod
    def evaluate(self, frame):
        pass