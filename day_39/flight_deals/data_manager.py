import requests, requests_cache

requests_cache.install_cache(
    'data_manager_cache',
    expire_after=600)

class DataManager:
    
    def __init__(self, key, auth, link):
        self.data = None
        self.get_sheet_url = link.replace("auth", key)
        self.header = {
            "Authorization": f"Bearer {auth}"
        }
        
    def get_sheet(self):
        try:
            get_sheet_r = requests.get(self.get_sheet_url, headers=self.header)
            get_sheet_r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"API Error : {e}")
            raise
        data = get_sheet_r.json()
        self.data = data["sheet1"]
        return self.data

    def get_budget_data(self):
        budgets = {}
        for d in self.data:
            dest = d["from"] + " to " + d["to"]
            budgets[dest] = d["budget"]
        return budgets
