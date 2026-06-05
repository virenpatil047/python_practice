import requests

MY_LAT = 18.580459
MY_LONG = 73.684402

# try:
#     response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=5)
#     response.raise_for_status()
#     data = response.json()
#     print("longitude : " + data["iss_position"]["longitude"])
#     print("latitude : c:\Users\viren\Downloads\kanye_quotes" + data["iss_position"]["latitude"])
# except requests.exceptions.RequestException as e:
#     print(e)


params = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted" : 0,
    "tzid" : "Asia/Kolkata"
}

try:
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = data["sunrise"].split("T")[1][:5]
    sunset = data["sunset"].split("T")[1][:5]

    print(f"Sunrise at : {sunrise}\nSunset at : {sunset}")
except requests.exceptions.RequestException as e:
    print(e)
