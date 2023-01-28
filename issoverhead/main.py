import requests
from datetime import datetime
import time 
import smtplib 

my_email = "example@mail.ru"
password = "example"

MY_LAT = 40.712776 # Your latitude
MY_LONG = -74.005974 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

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

time_now = datetime.now()

def send_mail(subject, sms, adress):
    with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
        from_addr=my_email, 
        to_addrs=adress, 
        msg=f"Subject:{subject}\n\n{sms}"
        )

def look():
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5 \
    and ((time_now.hour <= sunrise) or (time_now.hour >= sunset)):
        send_mail(subject="Look up!", sms="ISS in sky", adress="example@mail.ru")

while True:
    time.sleep(60)
    look()