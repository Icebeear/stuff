import pandas
import random
import smtplib 
import datetime as dt 

my_email = "example@mail.ru"
password = "example"

def send_mail(subject, sms, adress):
    with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
        from_addr=my_email, 
        to_addrs=adress, 
        msg=f"Subject:{subject}\n\n{sms}"
        )


data = pandas.read_csv("birthdays.csv")
users = data.to_dict(orient="records")
now = dt.datetime.now()
day = now.day

for date in users:
    if day == date["day"]:
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            wish = file.read()
        send_mail(subject="Happy Birthday!", sms=wish.replace("[NAME]", date["name"]), adress=date["email"])