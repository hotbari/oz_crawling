import requests
from bs4 import BeautifulSoup

# 이용자 정보 입력
header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

# 접속하고자 하는 주소 입력!
base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="

# base_url 뒤에 검색어 입력하면 해당 키워드를 검색한 url로 이동할 수 있다
search_url = input("검색어 입력 : ")
url = base_url + search_url

req = requests.get(url, headers = header_user)

h = req.text
soup = BeautifulSoup(h, "html.parser" )

news_tit = soup.select(".news_tit")
news_contents = soup.select(".news_contents")
info_press = soup.select(".thumb_box")

# 몇 번째 뉴스인지!
# j 선언을 바깥쪽에 해줘야 됐다
j = 0

for i in news_tit :
    if j <= len(news_tit):
        j+=1
        print(f"{j}번째 뉴스 : {i.text}")
    

# for i in range(len(news_tit)):
#     for j in news_tit :
#         print(f"뉴스{i+1} : {j.text}")
#     i += 1
# 이렇게 하면 뉴스 1 4개, 뉴스 2 4개 ... 이런 식