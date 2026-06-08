import os, requests
from twilio.rest import Client

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

link = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")

params = {
    "lat" : 18.579895,   # Pune
    "lon" : 73.684223,
    "cnt" : 4,
    "appid" : api_key
}

try:
    response = requests.get(link, params=params)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(e)
    raise
    
# print(response.status_code)
# with open("data.txt", "w") as f:
#     f.write(str(data))

# weather_id = data["list"][1]["weather"][0]["id"]
# weather_desc = data["list"][1]["weather"][0]["description"]
weather_ids = [data["list"][i]["weather"][0]["id"] for i in range(0, len(data["list"]))]
weather_descs = [data["list"][i]["weather"][0]["description"] for i in range(0, len(data["list"]))]
# print(f"weather_ids : {weather_ids}\nweather_descs : {weather_descs}")

if any(id < 700 for id in weather_ids):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today, don't forget to bring an umbrella ☂️.",
        from_="+13613044933",
        to="+91XXXXXXXXXX",
    )
    
    print(message.status)
