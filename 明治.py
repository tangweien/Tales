# 明治網站 爬巧克力標籤+網址+內文 並寫入txt

import urllib.request as req
url="https://www.meiji.co.jp/products/chocolate/"

request=req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"})

with req.urlopen(url) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data,"html.parser")

a1=root.find_all("div", class_="l-card-body")

print(a1)
for b1 in a1:
    win=b1.p.text.strip()
    print(win)
    with open("data.txt", mode="a", encoding="utf-8") as file:
        file.write(win+"\n")
    url = "https://www.meiji.co.jp/" + b1['href']
    # print(url)
    request=req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"})
    with req.urlopen(url) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data,"html.parser")

    c1=root.find_all("table", class_="m-table")
    for d1 in c1[0:]:
        lose=d1.tbody.text.strip()
        print(lose)
        with open("data.txt", mode="a", encoding="utf-8") as file:
            file.write(lose+"\n")
