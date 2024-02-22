from nutrition_scraper import *
from spreadsheet_editor import *

nutritionix_api = NutritionixAPI()
spreadsheet_editor = SpreadsheetEditor()

user_exercise = input('What exercise did you complete today? ')
nutritionix_api.data_generator(user_exercise)

# To do
# Pass response from exercise estimator into spreadsheet editor
spreadsheet_editor.insert()


