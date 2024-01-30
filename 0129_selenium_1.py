from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = "http://naver.com"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

# title = driver.title
# print(title) #창이 실행됐다가 종료되고 결과값이 출력됨

html = driver.page_source

# 셀레니움엔 파서 기능이 없어서 뷰숩 재소환
soup = BeautifulSoup(html, "html.parser")

query = soup.select_one("#query")
print(query)