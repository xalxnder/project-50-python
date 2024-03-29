from flight_checker import *
from spreadsheet_interface import *
from datetime import date, timedelta
from message_sender import *

flight_checker = FlightChecker()

spreadsheet_interface = SpreadsheetInterface()
PRICES_SPREADSHEET = spreadsheet_interface.read('prices')
USERS_SPREADSHEET = spreadsheet_interface.read('users')
message_sender = MessageSender()


TODAY = date.today().strftime("%d/%m/%Y")
is_adding_users = input('Do you want to add more users? (y/n): ')
SIX_MONTHS = (date.today() + timedelta(days=6 * 30)).strftime("%d/%m/%Y")
ORIGIN_IATA = 'PHL'

while is_adding_users == 'y' or is_adding_users == 'Yes':
    FIRST_NAME = input('What is your first name?: ')
    LAST_NAME = input('What is your last name?: ')
    EMAIL = input('What is your email?')
    is_adding_users = input('Do you want to add more users? (y/n): ')
    spreadsheet_interface.add_users(FIRST_NAME, LAST_NAME, EMAIL, 'users')

for i in PRICES_SPREADSHEET:
    print(i)
    city_column = i['city']
    code_column = i['iataCode']
    row_column = i['id']
    if code_column == '':
        iata_code = flight_checker.get_code(city_column)
        spreadsheet_interface.update_iata_codes(row_column, iata_code)


for cell in PRICES_SPREADSHEET:
    flight_checker.get_prices(ORIGIN_IATA, cell['iataCode'], TODAY, SIX_MONTHS)
    spreadsheet_price = cell['lowestPrice']
    try:
        new_price = flight_checker.prices[cell['iataCode']]
    except KeyError as e:
        print('Sorry, no price for that')
    else:
        if new_price < spreadsheet_price:
            message_sender.message += f'Only ${new_price} to fly from {ORIGIN_IATA} to {cell["iataCode"]}\n'

for user in USERS_SPREADSHEET:
    print(user['email'])
    # message_sender.send_message(user['email'])


# print(message_sender.message)
# message_sender.send_message()
