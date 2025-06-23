from abc import ABC, abstractmethod

class INotificationStrategy(ABC):
    @abstractmethod
    def send(self, message, user):
        pass
