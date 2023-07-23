import requests
from twilio.rest import Client 

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = API_KEY
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
weather_params = {
    "lat": -5.147665,
    "lon": 119.432732,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
# print(response.json()["hourly"][0]["weather"][0]["id"])
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_id = hour_data["weather"][0]["id"] 
    if condition_id < 700:
        will_rain = True

# if will_rain:
client = Client(account_sid, auth_token) 

message = client.messages.create(  
                            messaging_service_sid=messaging_service_sid, 
                            body="Today will be rainy", 
                            from_=from_phone_number,  
                            to=to_phone_number
                        ) 

print(message.sid)