from datetime import datetime as dt
from datetime import timedelta
from zoneinfo import ZoneInfo

DATE = (dt.now(ZoneInfo("Asia/Kolkata")) + timedelta(weeks=24)).strftime("%Y-%m-%d")
class FlightData:
    def __init__(self, sheet_data):
        self.flight_data = []
        self.budgets = []
        for sheet in sheet_data:
            self.flight_data.append({
                "engine": "google_flights",
                "departure_id": sheet["from"].upper(),
                "arrival_id": sheet["to"].upper(),
                "currency": "INR",
                "type": "2",
                "outbound_date": DATE
                })
            self.budgets.append(sheet["budget"])
    
    def get_flight_data(self):
        return self.flight_data
    
    def get_flight_budgets(self):
        return self.budgets
