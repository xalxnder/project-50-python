from nutrition_scraper import *
from spreadsheet_editor import *

nutritionix_api = NutritionixAPI()
spreadsheet_editor = SpreadsheetEditor()

user_exercise = input('What exercise did you complete today? ')
exercise_data = nutritionix_api.get_exercise_data(user_exercise)


spreadsheet_editor.insert(exercise_data)


