from flight_checker import *
from spreadsheet_editor import *

flight_checker = FlightChecker()


spreadsheet_editor = SpreadsheetEditor()
spreadhseet_data = spreadsheet_editor.read()


# for i in spreadhseet_data['prices']:
#     city_column = i['city']
#     code_column = i['iataCode']
#     row_column = i['id']
#     if code_column == '':
#         iata_code = flight_checker.get_code(city_column)
#         spreadsheet_editor.update_iata_codes(row_column, iata_code)

flight_checker.get_prices()

