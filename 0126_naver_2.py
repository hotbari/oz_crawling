## 트래픽 튕길 때 회피하는 법

import requests
from bs4 import BeautifulSoup

# 이용자 정보 입력
header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

url = "http://www.naver.com"

# url 요청자가 위의 이용자인 것처럼 속임
req = requests.get(url, headers=header_user)

print(req.Request)