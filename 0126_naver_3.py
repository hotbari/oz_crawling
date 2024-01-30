import requests
from bs4 import BeautifulSoup

# 이용자 정보 입력
header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=influencer&query=%EC%86%90%ED%9D%A5%EB%AF%BC&oquery=%EB%9D%BC%EC%9D%B4%EC%A6%88+%EC%9B%90%EB%B9%88&tqi=ikL6Twqo15Vss66kb1ZssssssFh-313851"
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

keyword_box = soup.select(".keyword_box_wrap.type_color")
titles = soup.select(".title_link._foryou_trigger")
names = soup.select(".name.elss")

n = 1  

for i in titles :
    print("--------------------")  

    if n <= 5 :
        title = i.text

        for j in names :
            name = j.text
            print(f"기사제목 : {title}")
            print(f"작성자 : {name}")
            print()
            n += 1

        
