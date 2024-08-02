from email_example import EmailService
import unittest
from unittest.mock import Mock

class TestEmailService(unittest.TestCase):

    def setUp(self):
        self.smtp_client = Mock()
        self.service = EmailService(self.smtp_client)

    def test_send_email(self):
        recipient = "test@example.com"
        subject = "Test Subject"
        body = "This is a test email."

        self.service.send_email(recipient, subject, body)

        self.smtp_client.send_message.assert_called_with({
            "to": recipient,
            "subject": subject,
            "body": body
        })

if __name__ == "__main__":
    unittest.main()
