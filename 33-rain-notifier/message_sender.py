import os
import smtplib


class MessageSender():
    def __init__(self, message):
        self.message = message

    def send_message(self):
        body = 'You might want to bring an umbrella. Rain is forecasted!'
        sender = ''
        recipient = ''
        password = ''
        connection = smtplib.SMTP()
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, to_addrs=recipient, msg=body)
        connection.close()
