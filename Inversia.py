class NotificationService:
    def send_notification(self, message):
        pass

class EmailNotification:
    def send_notification(self, message):
        print("Sending email notification: ", message)

class SMSNotification:
    def send_notification(self, message):
        print("Sending SMS notification: ", message)

class NotificationManager:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def send_notification(self, message):
        self.notification_service.send_notification(message)

email_notification = EmailNotification()
sms_notification = SMSNotification()

notification_manager_email = NotificationManager(email_notification)
notification_manager_email.send_notification("Hello, this is an email notification!")

notification_manager_sms = NotificationManager(sms_notification)
notification_manager_sms.send_notification("Hello, this is an SMS notification!")