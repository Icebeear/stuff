import requests
import datetime as dt 
import os 

now = dt.datetime.now()

app_id = os.environ.get("OWN_ID")
app_key = os.environ.get("OWN_KEY")
token = os.environ.get("OWN_TOKEN")

exercise = input("Tell me which exercises you did: ")

exercise_endoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query": exercise,
}

exercise_head = {
    "x-app-id": app_id,
    "x-app-key": app_key,
}

exercise_response = requests.post(url=exercise_endoint, json=exercise_params, headers=exercise_head)
data = exercise_response.json()

bearer_head = {
    "Authorization": f"Bearer {token}"
}

sheet_endpoint = "https://api.sheety.co/b23378e46f711b0114cbaefdbbda8173/myWorkouts/workouts"

for exercise in data["exercises"]:
    sheet_params = {
        "workout": {
                "date": f"{now.strftime('%x')}",
                "time": f"{now.strftime('%X')}",
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"] 
        }
    }
    add_row = requests.post(url=sheet_endpoint, json=sheet_params, headers=bearer_head)