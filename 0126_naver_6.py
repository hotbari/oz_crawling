import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

url = "https://www.naver.com/"

req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")

#find 활용법 select랑 유사한 기능
# soup.find(class_="link_service", text = "뉴스") 클래스명 뒤에 _ 붙이는 것 유의
# soup.find(id="link_service", text = "뉴스")

# soup.find_all