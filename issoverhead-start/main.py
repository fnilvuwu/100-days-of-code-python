import requests
import math
from datetime import datetime
import smtplib
import time

MY_LAT = -5.147665 # Your latitude
MY_LONG = 119.432732 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

while True:
    #If the ISS is close to my current position
    if math.sqrt((MY_LAT - iss_latitude)**2 + (MY_LONG - iss_longitude)**2) > 5 or math.sqrt((MY_LAT - iss_latitude)**2 + (MY_LONG - iss_longitude)**2) < -5:
        # and it is currently dark
        if time_now >= sunset and time_now <= sunrise:
            # Then send me an email to tell me to look up.
            email = EMAIL
            pw = PASSWORD

            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(email, pw)
            connection.sendmail(email, email, msg="Look at the sky for International Space Station!")
            connection.close()
    time.sleep(60)
# BONUS: run the code every 60 seconds.



