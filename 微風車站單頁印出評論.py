import requests 
import json
p = 0
while p <=5:
    url = f"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758526229655785!2y6996257486398011841!2m2!1i{p}0!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1siE2OYe_vLIHk2roPhee4kAo!7e81"
    text = requests.get(url).text
    pretext = ')]}\''
    text = text.replace(pretext,'')
    soup = json.loads(text)
    conlist = soup[2]

    for i in conlist:
        # print("username:"+str(i[0][1]))
        # print("time:"+str(i[1]))
        # print("comment:"+str(i[3]))
        afternoon_tea = [['username', str(i[0][1])],  ['time', str(i[1])], ['comment', str(i[3])]]
        win=dict(afternoon_tea)
        print(win)

        file = open("data.json", "a")
        json.dump(win, file)
        file.close()
    p+=1
    
# p一次可以印出10筆評論。
# 技術太差 怕拖累後續作業 如果評論很感的話可能要麻煩先用這個單頁印出評論『微風廣場車站的評論』
# 有包成字典轉JSON檔了。
