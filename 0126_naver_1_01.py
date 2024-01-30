#뷰숩으로 크롤링

import requests #requests를 불러옴
from bs4 import BeautifulSoup #bs4에서 BeautifulSoup 불러옴

# 이용자 정보를 입력한다
# 이용자 정보는 header에 저장된다

# 접속하고자 하는 주소(URL) 입력

url = "https://www.naver.com/"

# Get 방식을 이용해서 서버에게 Resource를 보내도록 요청한다.
# 데이터 수신이 가능하게 준비하는 것
# requests의 경우 거의 처음에 사용되고 이후에는 잘 사용되지 않는데 
# 정적사이트의 경우에는 html 코드가 잘 변하지 않기 때문이다.
# requests 패키지 안에 있는 get 메소드를 사용하고 이를 변수에 담는다.
# requests 로 넘어오는 내용은 페이지 소스보기로 보는 내용과 동일 ! ! 

req = requests.get(url)

# Get으로 가져온 데이터들 중 텍스트 형태의 자료를 변수에 담는다(html도 텍스트 문서!)

h = req.text

# 뷰숩은 2개의 파라미터를 받는다. 여기서는 h, "html.parser"
# BeautifulSoup(데이터, 데이터.. 파서?)

soup = BeautifulSoup(h, "html.parser")

# select_one 으로 원하는 태그를 찾을 수 있다(클래스명, id, 태그 등) 클래스는 . id는 #

query = soup.select_one(".dsc")
print(query)