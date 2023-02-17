from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from threading import Timer

state = True 

path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

mas = {}

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

def stop_play():
    global state
    state = False
Timer(30, stop_play).start()    

def check():
    money = driver.find_element(By.XPATH, '//*[@id="money"]').text.replace(",", "")
    store = driver.find_elements(By.CSS_SELECTOR, '#store b')[:-1:]
    for x in store[::-1]:
        x = x.text.split("-")
        mas[x[0]] = int(x[1].replace(",", ""))
    
    for key in mas:
        if mas[key] <= int(money):
            try:
                element = driver.find_element(By.ID, f"buy{key[:-1:]}")
                element.click()
                money = driver.find_element(By.XPATH, '//*[@id="money"]').text.replace(",", "")
                store = driver.find_elements(By.CSS_SELECTOR, '#store b')[:-1:]
                for x in store[::-1]:
                    x = x.text.split("-")
                    mas[x[0]] = int(x[1].replace(",", ""))
            except:
                print("It's not a error, everything is ok bro :)")
    if state:
        Timer(5, check).start()
check()

while state:
    cookie.click()

score = driver.find_element(By.XPATH, '//*[@id="cps"]').text 
print(score)