import requests

FLIGHT_HEADER = {
    "apikey": API_KEY
}
SHEET_URL = API_SHEET_URL
FLIGHT_SEARCH = "https://tequila-api.kiwi.com/v2/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        sheet_response = requests.get(url=SHEET_URL) 
        for item in sheet_response.json()["prices"]:
            flight_config = {
                "fly_from": "LON",
                "fly_to": item["iataCode"],
                "date_from": "05/04/2022",
                "date_to": "05/10/2022",
                "limit": "1",
            }

            flight_response = requests.get(url=FLIGHT_SEARCH, headers=FLIGHT_HEADER, params=flight_config) 
            flight_price = flight_response.json()["data"][0]["price"]
            dept_city = f'{flight_response.json()["data"][0]["cityFrom"]}-{flight_response.json()["data"][0]["flyFrom"]}'
            dest_city = f'{flight_response.json()["data"][0]["cityTo"]}-{flight_response.json()["data"][0]["flyTo"]}'
            dept_date = flight_response.json()["data"][0]["local_departure"][:10]
            arr_date = flight_response.json()["data"][0]["local_arrival"][:10]

            if item["lowestPrice"] > flight_price:
                print(f'Low price alert! Only ${flight_price} to fly from {dept_city} to {dest_city}, from {dept_date} to {arr_date}')


FlightSearch()