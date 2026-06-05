import requests, smtplib, time
from pathlib import Path
from datetime import datetime, timedelta

MY_LAT = 18.578758
MY_LONG = 73.683897

sender_email = "wren@gmail.com"
sender_pwd = "pwd"
reciever_email = "test@gmail.com"
base_path = Path(__file__).parent

def iss_overhead():
        
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    def send_mail():
        content = f"Subject: Look Up\n\n There's an ISS over your head now."
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.starttls()
            conn.login(sender_email, sender_pwd)
            conn.sendmail(
                from_addr=sender_email,
                to_addrs=reciever_email,
                msg=content
            )
            
    def check_positon():
        if (MY_LAT >= iss_latitude -5 and MY_LAT <= iss_latitude + 5) and (MY_LONG >= iss_longitude -5 and MY_LONG <= iss_longitude + 5):
            return True
        return False

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid" : "Asia/Kolkata"
        
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset:
        if check_positon():
            send_mail()

while True:
    iss_overhead()
    time.sleep(60)

        
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



