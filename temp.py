import time
from datetime import datetime
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import requests
import random
from bs4 import BeautifulSoup

proxy_list = [
    {"http": "http://43.153.207.93:3128", "https": "https://43.153.207.93:3128"},
]

client = MongoClient('mongodb://localhost:27000/')
db = client['twitter_trends']
collection = db['trends']

unique_id = str(int(time.time()))

driver = webdriver.Chrome(seleniumwire_options= {
    'proxy': proxy_list[0],
    })

# driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://x.com/i/flow/login')
driver.implicitly_wait(10)

username_field = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
username_field.send_keys('rrai39373@gmail.com')
next_button = driver.find_element(By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
next_button.click()

driver.implicitly_wait(10) 

password_field = driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
password_field.send_keys('Senti2002#')
login_button = driver.find_element(By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
login_button.click()

driver.implicitly_wait(100)

trends = driver.find_elements(By.XPATH, "//span[@class='css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1bymd8e']")

trendlist= []
for trend in trends:
    trendlist.append(trend.text)
print(trendlist)
ip_address = requests.get('https://api.ipify.org').text
print(ip_address)
# result = {
#     'unique_id': unique_id,
#     'trend1': trendlist[0],
#     'trend2': trendlist[1],

#     'timestamp': datetime.now(),
#     'ip_address': ip_address
# }
# collection.insert_one(result)
print("################################################################3")
driver.quit()