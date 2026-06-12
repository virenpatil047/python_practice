import os
from twilio.rest import Client
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
DATE = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d")
TO_DATE = (datetime.now(ZoneInfo("Asia/Kolkata")) + timedelta(weeks=24)).strftime("%Y-%m-%d")
class NotificationManager:
    
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
    
    def send_sms(self, dest, price):
        msg =   f"Low price alert! Only ₹{price} to fly from {dest}, on {DATE} until {TO_DATE}"
        message = self.client.messages.create(
            body=msg,
            from_="+13613044933",
            to="+918088343188",
        )
        # print(message.status)
