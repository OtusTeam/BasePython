class EmailService:
    def __init__(self, smtp_client):
        # smtp_client — это объект, который взаимодействует с SMTP-сервером
        self.smtp_client = smtp_client

    def send_email(self, recipient, subject, body):
        # Метод отправки электронного письма
        self.smtp_client.send_message({
            "to": recipient,
            "subject": subject,
            "body": body
        })
