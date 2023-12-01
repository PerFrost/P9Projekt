from abc import ABC, abstractmethod

class GestureCommand(ABC):
    @abstractmethod
    def execute(self):
        pass