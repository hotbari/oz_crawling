import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")

# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")

# lst_all = lst50 + lst100
# print(len(lst_all))


# find 문법으로 리팩토링
lst_all = soup.find_all(class_=["lst50","lst100"])

rank = 1

for i in lst_all : #for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a") #태그 선택할 때 띄어쓰고 걸면 됨
    singer = i.select_one(".ellipsis.rank02 a")
    album = i.select_one(".ellipsis.rank03 a")

    
    print(f"{rank}위 곡 정보 : {title.text} - {singer.text} \n 앨범명 : {album.text}")
    rank += 1
