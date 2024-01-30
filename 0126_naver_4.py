import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요 : ")
url = base_url + search_url

req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")

titles = soup.select(".title_link._cross_trigger")
title = soup.select(".title_area")
#바로 다음에 오는 태그 지칭! > 로 들어가기
user = soup.select(".user_info > a")



for i in zip(titles, user):
    # print(type(i))
    print(f"제목: {i[0].text}")
    print(f"작성자 : {i[1].text}")
    print(f"링크로 이동: {i[0]['href']}")
    print()

