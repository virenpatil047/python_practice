import serpapi
from notification_manager import NotificationManager

MAX = 2**31 - 1

class FlightSearch:
    def __init__(self, key):
        self.client = serpapi.Client(api_key=key)
        self.results = []
        self.lowest_prices = []
        self.notification_manager = NotificationManager()
        
    
    def search_flight(self, flight_data):
        for data in flight_data:
            result = self.client.search(data)
            self.results.append(result)
            try:
                self.lowest_prices.append(result["price_insights"]["lowest_price"])
            except:
                self.lowest_prices.append(MAX)

    def get_flight_data(self):
        return self.results
    
    def get_lowest_prices(self):
        return self.lowest_prices
    
    def send_sms(self, budgets):
        for price, dest in zip(self.lowest_prices, budgets.keys()):
            if price < budgets[dest]:
                self.notification_manager.send_sms(dest, price)
