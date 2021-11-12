import requests 
import json
p = 0
while p <=3:
    url = f"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3773258091363931747!2y2127068001886947614!2m2!1i{p}!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1snaGLYZQB9OHaug_Wg5nYCA!7e81"
    # 發送get請求
    text = requests.get(url).text
    # 取代掉特殊字元，這個字元是為了資訊安全而設定。
    pretext = ')]}\''
    text = text.replace(pretext,'')
    # 把字串讀取成json
    soup = json.loads(text)
    # 取出包含留言的List 。
    conlist = soup[2]
    # 逐筆抓出
    for i in conlist:
        print("username:"+str(i[0][1]))
        print("time:"+str(i[1]))
        print("comment:"+str(i[3]))
    p+=1
