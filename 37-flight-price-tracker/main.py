from flight_checker import *
from spreadsheet_editor import *
from datetime import date, timedelta

flight_checker = FlightChecker()


spreadsheet_editor = SpreadsheetEditor()
spreadhseet_data = spreadsheet_editor.read()

TODAY = date.today().strftime("%d/%m/%Y")
SIX_MONTHS = (date.today() + timedelta(days=6*30)).strftime("%d/%m/%Y")
FLIGHTS_SPREADSHEET = spreadhseet_data['prices']
ORIGIN_IATA = 'PHL'

# for i in spreadhseet_data['prices']:
#     city_column = i['city']
#     code_column = i['iataCode']
#     row_column = i['id']
#     if code_column == '':
#         iata_code = flight_checker.get_code(city_column)
#         spreadsheet_editor.update_iata_codes(row_column, iata_code)


for cell in FLIGHTS_SPREADSHEET:
    flight_checker.get_prices(ORIGIN_IATA, cell['iataCode'], TODAY, SIX_MONTHS)



for cell in FLIGHTS_SPREADSHEET:
    spreadsheet_price = cell['lowestPrice']
    try:
        new_price = flight_checker.prices[cell['iataCode']]
    except KeyError as e:
        print('Sorry, no price for that')
    else:
        if new_price < spreadsheet_price:
            print('FOUND LOWER PRICE')

