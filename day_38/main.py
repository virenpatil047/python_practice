import os, requests
from datetime import datetime as dt
from zoneinfo import ZoneInfo

BASE_URL = "https://app.100daysofpython.dev"
NUTRI_POST = f"{BASE_URL}/v1/nutrition/natural/exercise"
SHEETY_KEY = os.getenv("SHEETY_KEY")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
SHEETY_POST = f"https://api.sheety.co/{SHEETY_KEY}/workouts/workouts"
HEADERS = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("APP_KEY")
}
NOW = dt.now(ZoneInfo("Asia/Kolkata"))

def get_nutri_response(q):
    try:
        nutri_post_params = {"query": q}
        nutri_post_r = requests.post(NUTRI_POST, json=nutri_post_params, headers=HEADERS)
        nutri_post_r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"API Error : {e}")
    
    data = nutri_post_r.json()
    exercise, duration, calories = data['exercises'][0]['name'], data['exercises'][0]['duration_min'], data['exercises'][0]['nf_calories']
    date, time = NOW.strftime("%d/%m/%Y"), NOW.strftime("%H:%M:%S")
    data_for_sheet = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }
    
    return data_for_sheet

def update_sheet(data):
    try:
        sheety_header = {
            "Authorization": f"Bearer {SHEETY_AUTH}"
        }
        sheety_post_r = requests.post(SHEETY_POST, json=data, headers=sheety_header)
        sheety_post_r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"API Error : {e}")

query = input("Tell me what exercise what you did : ").lower()
if "and" in query:
        querys = query.split("and")
        for q in querys:
            data = get_nutri_response(q)
            update_sheet(data)
else:
    data = get_nutri_response(query)
    update_sheet(data)

print("Done")
