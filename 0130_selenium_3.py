from selenium import webdriver
from bs4 import BeautifulSoup
import time

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요 : ")
url = base_url + search_url

driver = webdriver.Chrome()
driver.get(url)

time.sleep(1)

# 스크롤 코드 0px~4000px
# driver.execute_script("window.scrollTo(0,4000)")
# time.sleep(2)

# 끝까지 스크롤 내리려면
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(5)

for i in range(5) :
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")

areas = soup.select(".view_wrap")

num = 1
for i in areas :
    titles = i.select_one(".title_link._cross_trigger")
    name = i.select_one(".user_info > a")
    print(num)
    print(titles.text)
    print(name.text)
    print()

    num += 1


