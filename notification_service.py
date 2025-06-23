from INotificationStrategy import INotificationStrategy

class NotificationService:
    def __init__(self, strategy: INotificationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: INotificationStrategy):
        self._strategy = strategy

    def notify(self, message, user):
        self._strategy.send(message, user)
