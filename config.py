import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -41.9684
MY_LONG = -41.4704
MY_EMAIL = YOUR_EMAIL
GMAIL_SERVER = "smtp.gmail.com"
# declare an application in your Google account settings, security section --> 2-step verification: Google will give you a unique password
MY_PASSWORD = YOUR_PASSWORD 


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print("data -->", data)

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and ( MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True


def is_night_time():
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
    print("sunrise -->", sunrise)
    print("sunset -->", sunset)

    time_now = datetime.now().hour
    print("time_now -->", time_now)

    if time_now <= sunrise or time_now >= sunset:
        # print("it's night time")
        return True


# BONUS: run the code every 60 seconds.
check_on = True
while check_on:
    if True and True:
        check_on = False
        print("look")
        with smtplib.SMTP(GMAIL_SERVER, 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:Look up!\n\nISS is over you head!")
    else:
        print("not yet")
    time.sleep(60)





