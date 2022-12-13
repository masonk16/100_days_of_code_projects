import time
import requests
from datetime import datetime
import smtplib

MY_LAT = -17.766150
MY_LONG = 30.979220

EMAIL = "grey.pafotisevheni@yahoo.com"
PASSWORD = "wllaqeaotxnaitmu"


def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
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

    curr_hour = datetime.now().hour

    if curr_hour >= sunset or curr_hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_close and is_night:
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)

            # Send email
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="grey.pafotisevheni@yahoo.com",
                msg=f"Subject: Look up! \n\n Look out for the ISS."
            )

