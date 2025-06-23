from INotificationStrategy import INotificationStrategy

class EmailNotification(INotificationStrategy):
    def send(self, message, user):
        print(f"Email для {user}: {message}")

class PushNotification(INotificationStrategy):
    def send(self, message, user):
        print(f"Push уведомление для {user}: {message}")

class SmsNotification(INotificationStrategy):
    def send(self, message, user):
        print(f"SMS для {user}: {message}")
