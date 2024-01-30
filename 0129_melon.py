import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")

song_title = soup.select(".ellipsis.rank01")
singer = soup.select(".ellipsis.rank02")



rank = []

for i in zip(song_title,singer):
    print(i.text)