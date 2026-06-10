import os, serpapi
from data_manager import DataManager
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()

SHEETY_KEY = os.getenv("SHEETY_KEY")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
SERP_KEY=os.getenv("SERP_KEY")
SHEETY_GET_URL = "https://api.sheety.co/auth/flightTracker/sheet1" 
SERP_GET_URL = "https://serpapi.com/search?"
DATE = dt.now()

data_manager = DataManager(SHEETY_KEY, SHEETY_AUTH, SHEETY_GET_URL)
flight_data = data_manager.get_sheet()

client = serpapi.Client(api_key="")
results = client.search({
  "engine": "google_flights",
  "departure_id": "CDG",
  "arrival_id": "AUS",
  "currency": "INR",
  "type": "2",
  "outbound_date": DATE.strftime("%Y-%m-%d")
})
best_flights = results["best_flights"]