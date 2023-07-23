import requests

FLIGHT_HEADER = {
    "apikey": API_KEY
}
SHEET_URL = API_SHEET_URL
FLIGHT_URL = "https://tequila-api.kiwi.com/locations/query"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        sheet_response = requests.get(url=SHEET_URL) 
        for item in sheet_response.json()["prices"]:
            flight_config = {
                "term": item["city"],
                "limit": "1"
            }

            flight_response = requests.get(url=FLIGHT_URL, headers=FLIGHT_HEADER, params=flight_config) 
            
            sheet_json = {
                "price": {
                    "iataCode": flight_response.json()["locations"][0]["code"],
                }
            }
            requests.put(url=f"""{SHEET_URL}/{item["id"]}""", json=sheet_json) 
            print(flight_response.json()["locations"][0]["code"])
            print(f"""{SHEET_URL}/{item["id"]}""")

            
        print(sheet_response.json()["prices"])


data = DataManager()