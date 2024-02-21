from nutrition_scraper import *

nutritionix_api = NutritionixAPI()

user_exercise = input('What exercise did you complete today? ')
nutritionix_api.exercise_estimator(user_exercise)
