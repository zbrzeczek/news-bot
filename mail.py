import smtplib
from email.message import EmailMessage

class Mail():
    def __init__(self, message):
        self.message = message
        self.sender = None
        self.receiver = None

    def set_receiver(self, receiver):
        self.receiver = receiver

    def set_sender(self, sender):
        self.sender = sender

    def send(self, message):
        msg = EmailMessage()
        print(message)
        msg.set_content(message[1])
        msg["Subject"] = message[0]
        msg["From"] = self.sender
        msg["To"] = self.receiver

        with smtplib.SMTP("localhost", 1025) as server:
            server.send_message(msg)

        print("Email sent locally!")
