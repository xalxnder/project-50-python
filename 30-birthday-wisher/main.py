import smtplib
import pandas as pd
from datetime import datetime
import os
from random import randint

DATA_LOCATION = 'data/birthdays.csv'
DATA_CSV = pd.read_csv(DATA_LOCATION, delimiter=",")
BIRTHDAYS = DATA_CSV.to_dict(orient="records")
TODAY_DAY = datetime.now().day
TODAY_MONTH = datetime.now().month
TODAY_YEAR = datetime.now().year
LIST_OF_MESSAGES = os.listdir('messages')
RANDOM_MESSAGE = LIST_OF_MESSAGES[randint(0, len(LIST_OF_MESSAGES) - 1)]

email = input("Please enter your email address: ")


def is_birthday():
    matched_birthday = []
    for birthday in BIRTHDAYS:
        if birthday['Month'] == TODAY_MONTH and birthday['Day'] == TODAY_DAY:
            matched_birthday.append(birthday)
    if len(matched_birthday) > 0:
        return True, matched_birthday


def message_generator(recipient):
    with open(f'messages/{RANDOM_MESSAGE}', 'r') as message:
        contents = message.read()
        new = contents.replace('[NAME]', recipient)
    return new


if is_birthday():
    matched_birthdayss = is_birthday()[1]
    for i in matched_birthdayss:
        recipient = i['Name']
        final_message = message_generator(recipient)
        print(final_message)
        password = ""
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=final_message)
        connection.close()
