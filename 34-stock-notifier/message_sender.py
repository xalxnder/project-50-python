import os
import smtplib


class MessageSender:
    def __init__(self):
        self.sender = ''
        self.recipient = ''
        self.password = os.environ['SMTLIB_PASSWORD']

    def send_message(self, message):
        body = message.encode('utf-8')
        sender = self.sender
        recipient = self.recipient
        password = self.password
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, to_addrs=recipient, msg=body)
        connection.close()
