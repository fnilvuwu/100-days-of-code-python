import requests
from datetime import datetime

EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

EXERCISE_HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    # "x-remote-user-id": "0",
}

SHEET_URL = "https://api.sheety.co/432a69a7854af2151fc7867620b60e2d/myWorkouts/workouts"
today = datetime.now()
# current_hour = datetime.now().hour
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%H:%M:%S"))

SHEET_HEADER = {
    "Authorization": "Basic Zm5pbHZ1OnF3ZXJ0eTEyMw=="
}


exercies_config = {
    "query": input("Tell me which exercise you did: "),
}


response_exercise = requests.post(
    url=EXERCISE_URL, headers=EXERCISE_HEADERS, json=exercies_config)
sheet_config = {
    "workout": {
        "time": today.strftime("%H:%M:%S"),
        "date": today.strftime("%d/%m/%Y"),
        "exercise": response_exercise.json()["exercises"][0]["user_input"].title(),
        "duration": response_exercise.json()["exercises"][0]["duration_min"],
        "calories": int(response_exercise.json()["exercises"][0]["nf_calories"]),
    }
}
response_sheet = requests.post(
    url=SHEET_URL, json=sheet_config, headers=SHEET_HEADER)

print(response_sheet.text)
