from bs4 import BeautifulSoup
import urllib.request as req
import requests
import json
def getData(url):
    request=req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=BeautifulSoup(data,"html.parser")
    x=root.find_all("span", class_="search_list_box")

    import requests  # 出現847時 代入下方套件 關閉安全請求警告
    requests.packages.urllib3.disable_warnings()

    pg = 1
    for y in x:
        z1 = y.h2.string
        z2 = y.a["href"]
        print(f"{sum}-{pg}： ", z1, z2)
        # with open("data1.txt", mode="a", encoding="utf-8") as file:
        #     file.write(f"{sum}-{pg}： " + z1 + "\n")
        pg+=1
        response = requests.get(z2, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")
        article = soup.select('script[type="application/ld+json"]')[0].contents[0]
        results = json.loads(article, strict=False) # 取消json格式化，https://blog.csdn.net/u012928324/article/details/79800333
        final = results['articleBody']
        abc = final.replace('&nbsp', '\n')
        
        print("文章： " + abc + "\n")  # 字串更換後加入換行
        # with open("data1.txt", mode="a", encoding="utf-8") as file:
        #     file.write("文章： " + abc + "\n")
        
from urllib.parse import quote
a = input("請搜尋關鍵字: ")
b = quote(a.encode("utf-8")) # encode non-ASCII characters to ASCII characters 轉轉轉
c = int(input("1頁=25則新聞: "))

sum = 1
while sum <= c:
    paguURL=f"https://news.tvbs.com.tw/news/searchresult/{b}/news/" + str(sum)
    print(f"新聞第 {sum} 頁", paguURL)
    getData(paguURL)
    sum+=1
