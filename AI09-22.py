from selenium.webdriver import Chrome
from urllib.parse import quote
import time
a = input("請搜尋關鍵字: ")
b = quote(a.encode("utf-8"))
driver=Chrome("./chromedriver")
driver.get(f"https://www.google.com/maps/place?q={b}")
ps=driver.find_elements_by_class_name("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")
urls = [l.get_attribute('href') for l in ps]

for u in urls:
    time.sleep(3) 
    driver.get(u)
    driver.find_element_by_class_name("h0ySl-wcwwM-E70qVe-list").click() # 進入印出網頁後 還要再設定 點擊 進入評論網頁
    time.sleep(3)

    win=1 # 滾動頁面 可以抓更多 目前設定滾動2次
    while win<=2:
        pane = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
        time.sleep(3)
        win+=1

    ps1=driver.find_elements_by_class_name("ODSEW-ShBeI-title") # 用戶名稱
    ps2=driver.find_elements_by_class_name("ODSEW-ShBeI-text")  # 用戶評論

    for i in range(len(ps1)):
            print(ps1[i].text + '---' + ps2[i].text)

    # driver.back() # 回上一頁
    # driver.back() # 回上一頁
    # driver.close() # 關閉網頁
