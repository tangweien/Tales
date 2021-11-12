# 氣象站

import requests,prettytable
from bs4 import BeautifulSoup
 
b0=requests.get(
    "https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html",
        headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
        "Cookie":"TS010c55bd=0107dddfefb3bf9dbfbbd50b4c648e733b7838670b73b785f149aa1787c11e623cab600f4bebc512d38fce2bdeee6a0f88757bf67a; TS558d33eb027=08dc4bbcbbab2000a85d1f25a5596c88098b0a43cf87d5b02c3f0e527a7a4799a2aefb0c15f3ec80085cf96135113000ee3339184ab2f8aceb52c8d17a96429dbc7f4709521c1096cc721d79cd09f2f731e60db5d1badd837d1123d30428fc48; _ga_K6HENP0XVS=GS1.1.1634095943.1.0.1634095943.0; _ga=GA1.3.499177308.1634095943; _gid=GA1.3.334180729.1634095943; _gat_gtag_UA_126485471_1=1"
    }
)

b1=BeautifulSoup(b0.text,"html.parser")

b2 = b1.find_all("tr")                              # 找到包覆的tr代入變數

win=prettytable.PrettyTable(["縣市", "溫度"])        # PrettyTable 包覆文字框架
for b3 in b2:
    x = b3.find("th").text                          # 抓出縣市
    y = b3.find("span", {"class": "tem-C"}).text    # 抓出溫度
    win.add_row([x, y])                             # PrettyTable 包覆文字框架
print(win)                                          # 放到外面 印出完整一筆 放到裡面跑一次印一次

# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆分隔線☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

# 這個url應該會更新資料，更新時間都有在刷新

import requests
from bs4 import BeautifulSoup
import prettytable as pt

# 用檢查挖出來有存放最高氣溫的觀測站資料，看起來氣象局網站是做一個框架，把資料填進去，底下url應該是塞進去的即時資料
url = "https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html"
resp = requests.get(url)

source = BeautifulSoup(resp.text, "html.parser")        # 把resp.text放進bs裡面去搜尋HTML標籤

# 資料裡有一筆是資料時間，印出來觀察，後續確認如果網址不加時間戳記，是否可取得正確資料？
data_time = source.find("tr", attrs={"data-subtitle": '今日各縣市高溫測站資料'}).attrs['data-updatetime']
print(f"資料更新時間： {data_time}")

table = pt.PrettyTable(["縣市名稱", "高溫(C)"])          # 做一個prettytable來存資料
data_row = source.find_all("tr")                        # 所有的資料都存在tr標籤中，抓出data_row這個list來做for迴圈

for data in data_row:
    city = data.find("th").text                         # 抓出每一筆data裡面，存放city和temp資料的標籤
    temp = data.find("span", {"class": "tem-C"}).text
    table.add_row([city, temp])                         # 加資料到prettytable中
print(table)
