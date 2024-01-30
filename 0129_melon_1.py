import requests
from bs4 import BeautifulSoup
import datetime

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

url = "https://www.melon.com/chart/day/index.htm"

req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html, "html.parser")


#find 함수 쓸 때 클래스명에 . 필요X
lst = soup.find_all(class_=["lst50","lst100"])
day = soup.select_one(".year")

down_song = []
up_song = []



#enumerate 쓸 때 순서 중요! rank 파라미터가 먼저 와야 함!!
for rank ,i in enumerate(lst, 1):
    titles = i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".ellipsis.rank02 a")
    down = i.select_one(".down")
    up = i.select_one(".up")




    print(f"{day.text} 일간차트 {rank}위")
    print(f"<{titles.text}> - {singer.text}")

    

    if down :
        print(f"순위변동 : {down.text}단계 하락")
        if int(down.text) > 3 :
            down_song.append([titles.text + " - " + down.text + "단계 하락"])
    
    elif up :
        print(f"순위변동 : {up.text}단계 상승")
        if int(up.text) > 3 :
            up_song.append([titles.text+ " - " + up.text + "단계 상승"])


    else :
        print(f"순위변동없음(-)")
    
    print()

print(f"일간순위 급상승곡: {up_song}")
print(f"일간순위 급하강곡: {down_song}")
