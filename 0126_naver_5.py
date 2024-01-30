import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요 : ")
url = base_url + search_url

req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")

areas = soup.select(".view_wrap")


ad_box = soup.select(".bx.type_ad > title_area")
view_wrap = soup.select(".view_wrap")


ad_count = 0
for i in areas:   
    ad = i.select_one(".link_ad")
    if ad :
        ad_count += 1
        #continue #print("광고") 대신에 넘어가게 만들기!
    else :
        titles = i.select_one(".title_link._cross_trigger")
        name = i.select_one(".user_info > a")

        print(f"제목 : {titles.text}")
        print(f"작성자 : {name.text}")
        print()
    
print(f"광고 개수: {ad_count}")

    