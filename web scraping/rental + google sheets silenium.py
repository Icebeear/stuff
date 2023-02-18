import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

head = {
    "Accept-Language": "example",
    "User-Agent": "example",
}

GOOGLE_URL = "https://forms.gle/Dxj1G8omEH29bQ5Z8"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.884030776813404%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.666392961164114%2C%22west%22%3A-122.63417331103516%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A12%7D" 

response = requests.get(url=ZILLOW_URL, headers=head)
data = response.text
soup = BeautifulSoup(data, "html.parser")

prices = [price.text.split("+")[0] for price in soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-84-2__sc-yipmu-0 gugdBn")[:-1:]]

addresses = [adress.text for adress in soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-84-2__sc-yipmu-0 cTLZKy property-card-link")]

links = [link["href"] for link in soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-84-2__sc-yipmu-0 cTLZKy property-card-link")]

path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get(GOOGLE_URL)
time.sleep(1)

for adress, price, link in zip(addresses, prices, links):
    first = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    first.send_keys(adress)
    second.send_keys(price)
    if link[0] == "/":
       link = f"zillow.com{link}"
    third.send_keys(link)
    submit.click()
    retry = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    retry.click()