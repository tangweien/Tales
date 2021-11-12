# PCHome
# 重複輸入搜尋物和頁面

import requests,json,prettytable
x = input('搜尋關鍵字: ')
y = 1
while True:
    r1=requests.get(
        "https://ecshweb.pchome.com.tw/search/v3.3/all/results",
        params={
            'q':x,
            'page':y,
            'sort':'sale/dc'}
    )
    d=json.loads(r1.text)
    t1=prettytable.PrettyTable(["品項","金額"], encoding="utf8")
    t1.align["品項"]="l"
    t1.align["金額"]="r"

    for a in d["prods"]:
        t1.add_row([a["name"],a['price']])
    print(t1)
    y = input('搜尋頁面: ')
import requests,json,prettytable
while True:
    r1=requests.get(
        "https://ecshweb.pchome.com.tw/search/v3.3/all/results",
        params={
            'q':input('搜尋關鍵字: '),
            'page':input('搜尋頁面: '),
            'sort':'sale/dc'}
    )
    d=json.loads(r1.text)
    t1=prettytable.PrettyTable(["品項","金額"], encoding="utf8")
    t1.align["品項"]="l"
    t1.align["金額"]="r"

    for a in d["prods"]:
        t1.add_row([a["name"],a['price']])
    print(t1)

# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆分隔線☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

# 蝦皮

import requests, json
import prettytable as pt

keyword = ""
while keyword == "":
    keyword = input("搜尋Shopee蝦皮 - 關鍵字： ")

goto_page = 0
while True:    
    url = "https://shopee.tw/api/v4/search/search_items"
    # 等一下search裡面的q值可以塞變數，page的欄位也要可以塞變數
    search = {
        "by": "relevancy",
        "keyword": keyword,
        "limit": 20,
        "newest": (goto_page - 1) * 20,
        "order": "desc",
        "page_type": "search",
        "scenario": "PAGE_GLOBAL_SEARCH",
        "version": 2,
    }

    resp = requests.get(url, params=search)
    data = resp.json()["items"]

    table = pt.PrettyTable(["名稱", "價格"], encoding = "utf-8")
    table.align = "l"

    for item in data:
        product_name = item["item_basic"]["name"]
        list_price = round(item["item_basic"]["price"] / 100000)
        table.add_row([product_name, list_price])

    print(table)
    get_page = input("頁碼：")
    if get_page == "quit":
        break
    else:
        goto_page = int(get_page)
