from notifications import EmailNotification, PushNotification, SmsNotification
from notification_service import NotificationService

def main():
    user = "Иван"
    service = NotificationService(EmailNotification())
    service.notify("Добро пожаловать на курс!", user)

    service.set_strategy(PushNotification())
    service.notify("Занятие начнётся через 10 минут", user)

    service.set_strategy(SmsNotification())
    service.notify("Занятие отменено", user)

if __name__ == "__main__":
    main()
