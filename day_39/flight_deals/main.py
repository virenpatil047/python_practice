import os
from data_manager import DataManager
from dotenv import load_dotenv
from datetime import datetime as dt
from flight_data import FlightData
from flight_search import FlightSearch

load_dotenv()

SHEETY_KEY = os.getenv("SHEETY_KEY")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
SERP_KEY = os.getenv("SERP_KEY")
SHEETY_GET_URL = "https://api.sheety.co/auth/flightTracker/sheet1" 
SERP_GET_URL = "https://serpapi.com/search?"
DATE = dt.now()

data_manager = DataManager(SHEETY_KEY, SHEETY_AUTH, SHEETY_GET_URL)
sheet_data = data_manager.get_sheet()
budget_data = data_manager.get_budget_data()
print(budget_data)
# print("--------------------")
flight_data = FlightData(sheet_data)
search_data  = flight_data.get_flight_data()
# print(search_data)
# print("--------------------")
flight_search = FlightSearch(SERP_KEY)
flight_search.search_flight(search_data)
# flight_search_data = flight_search.get_flight_data()
# lowest_prices = flight_search.get_lowest_prices()
# print(flight_search_data)
# print(lowest_prices)
flight_search.send_sms(budget_data)