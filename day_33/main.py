import requests

try:
    response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=5)
    response.raise_for_status()
    data = response.json()
    print("longitude : " + data["iss_position"]["longitude"])
    print("latitude : " + data["iss_position"]["latitude"])
except requests.exceptions.RequestException as e:
    print(e)
