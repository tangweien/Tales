from selenium.webdriver import Chrome
from urllib.parse import quote
import time
a = input("請搜尋關鍵字: ")
b = quote(a.encode("utf-8"))
driver=Chrome("./chromedriver")
driver.get(f"https://www.google.com/maps/place?q={b}")
ps=driver.find_elements_by_class_name("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")

for ps1 in ps:
    url=ps1.get_attribute("href")
    print(url)
    time.sleep(3) 
    driver.get(url)
    driver.find_element_by_class_name("h0ySl-wcwwM-E70qVe-list").click() # 進入印出網頁後 還要再設定 點擊 進入評論網頁
    time.sleep(3)

    win=1 # 滾動頁面 可以抓更多 目前設定滾動5次
    while win<=5:
        pane = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
        time.sleep(5)
        win+=1

    ps1=driver.find_elements_by_class_name("ODSEW-ShBeI-title") # 用戶名稱
    # ps2=driver.find_elements_by_class_name("ODSEW-ShBeI-text")  # 用戶評論
    for x in ps1:
        print(x.text) # 用戶名稱
    print("=分隔線=")
    # for y in ps2:
    #     print(y.text) # 用戶評論

    # driver.back() # 回上一頁
    # driver.back() # 回上一頁
    # driver.close() # 關閉網頁