import requests
from datetime import datetime
import pytz
import smtplib

my_email = "Your mail"
password = "***********"
utc = pytz.utc
local_tz = pytz.timezone("Asia/Kolkata")

# Your latitude
MY_LAT = {Your latitude}
# Your longitude
MY_LONG = {Your Longitude}

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
if 5 > iss_latitude - MY_LAT > -5 and 5 > iss_longitude - MY_LONG > -5:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_utc_str = data["results"]["sunrise"]
    sunset_utc_str = data["results"]["sunset"]

    sunrise_utc = datetime.strptime(sunrise_utc_str, "%Y-%m-%dT%H:%M:%S+00:00")
    sunset_utc = datetime.strptime(sunset_utc_str, "%Y-%m-%dT%H:%M:%S+00:00")

    sunrise_local = utc.localize(sunrise_utc).astimezone(local_tz)
    sunset_local = utc.localize(sunset_utc).astimezone(local_tz)

    time_now = datetime.now()

    if time_now.hour > sunset_local.hour:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="{to address}", msg="HEY! Look up! ISS is above you")


