import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/dp/B0B727YMJT/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0?th=1"

head = {
    "Accept-Language": "example",
    "User-Agent": "example",
}

response = requests.get(url=URL, headers=head)
soup = BeautifulSoup(response.text, "lxml")
price = soup.find(class_="a-offscreen").text
real_price = float(price.split("$")[1])

item = soup.find(class_="a-size-large product-title-word-break").text

if real_price < 100:
    with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
        connection.starttls()
        connection.login(user="example", password="example")
        connection.sendmail(
        from_addr="example", 
        to_addrs="example", 
        msg=f"Subject:Amazon Price Alert!\n\n{item} is now ${real_price}\n{URL}"
        )