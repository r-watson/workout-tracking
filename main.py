import os
from dotenv import load_dotenv
import requests
from datetime import datetime

GENDER = "male"
WEIGHT = 72
HEIGHT = 172
AGE = 35

load_dotenv("C:\Programming\EnviornmentVariables\.env.txt")
NUTRIONIX_ID = os.getenv("NUTRIONIX_ID")
NUTRIONIX_KEY = os.getenv("NUTRIONIX_KEY")
NUTRIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrionix_headers = {
    "x-app-id": NUTRIONIX_ID,
    "x-app-key": NUTRIONIX_KEY,
}
# user_input = input("Tell me which exercise you did: ")
user_input = "I walked 5 miles"

nutrionix_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S %p")
print(today, time)
response = requests.post(NUTRIONIX_ENDPOINT, json=nutrionix_params, headers=nutrionix_headers)
result = response.json()
result_exercise = result["exercises"]
print (result_exercise)
exercise_name = result_exercise[0]["user_input"].upper()
duration = round(result_exercise[0]["duration_min"])
calories = round(result_exercise[0]["nf_calories"])

sheety_record = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories,
    }
}

print(sheety_record)

sheety_user = os.getenv("SHEETY_USERNAME")
sheety_project = "workoutTracking"
sheety_sheet = "workouts"

sheety_endpoint = f"https://api.sheety.co/{sheety_user}/{sheety_project}/{sheety_sheet}"

# sheety_record = {
#   "workout": {
# 	"date": "Syed K",
# 	"time": "syed@gmail.com",
#     "exercise": ,
#     "duration": ,
#     "calories"": ,
#   }
# }

sheety_add_row = requests.post(sheety_endpoint, json=sheety_record)