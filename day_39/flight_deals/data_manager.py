import requests, requests_cache

requests_cache.install_cache(
    'data_manager_cache',
    expire_after=600)

class DataManager:
    
    def __init__(self, key, auth, link):
        
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
        return data["sheet1"]
