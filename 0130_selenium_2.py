from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url = "https://section.cafe.naver.com/ca-fe/home"

# 뷰숩 이용했을 때
# req = requests.get(url)
# html = req.text

driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source

print(html)