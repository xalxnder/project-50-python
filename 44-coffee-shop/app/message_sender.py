import os
import smtplib


class MessageSender():
    def __init__(self, message, recipient):
        self.message = message
        self.password = os.environ['SMTLIB_PASSWORD']
        self.recipient = recipient


    def send_message(self):
        body = self.message
        sender = ''
        recipient = self.recipient
        password = self.password
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.connect(host='smtp.gmail.com', port=587)  # Connect to the SMTP server
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, to_addrs=recipient, msg=body)
        connection.close()
