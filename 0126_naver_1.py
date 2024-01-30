import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"

#requests는 거의 처음에 사용되면 이후에 사용x 정적사이트에서는 코드가 변하지 않기 때문에
#get 방식을 이용해서 서버에게 resource(자원)을 보내도록 요청, 데이터 수신이 가능하도록 준비시킴

req = requests.get(url)
# print(req)

# 텍스트 형태의 자료(html이 포한됨)을 가져옴
html = req.text

# 컴퓨터를 이해시키기 위한 뷰숩 함수 - 파서가 html을 트리구조로 분해
soup = BeautifulSoup(html,"html.parser")

# 원하는 태그(.클래스명, #id, tag도 가능) 1개 찾기
query = soup.select_one("#query")
print(query)