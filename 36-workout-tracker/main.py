from nutrition_scraper import *
from spreadsheet_editor import *

nutritionix_api = NutritionixAPI()
spreadsheet_editor = SpreadsheetEditor()

user_exercise = input('What exercise did you complete today? ')
exercise_data = nutritionix_api.get_exercise_data(user_exercise)

# To do
# Pass response from exercise estimator into spreadsheet editor
# spreadsheet_editor.insert()


