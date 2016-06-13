import time
from selenium import webdriver
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep    

mail_dict={}

URL = "https://www.cs.ccu.edu.tw/"
print("setting up Firefox")
i=0
browser = webdriver.Firefox()
browser.get(URL); # 前往 資工所 首頁
time.sleep(3) # 等待5秒
Table_01=browser.find_element_by_id('Table_01')
for4 = browser.find_element_by_xpath("//tbody/tr/td/b/a")
index= browser.find_element_by_link_text('中文').click() #點選中文


# 首頁
In_1 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[2]")
quicklink = browser.find_element_by_css_selector("div[class='quicklink']")
department_m = browser.find_elements_by_partial_link_text('系所辦公室')[0]
print(department_m.get_attribute("href")) #所辦的mail
i=i+1
camp_m = browser.find_elements_by_partial_link_text('資工營信箱')[0]
print(camp_m.get_attribute("href")) #營隊的mail
i=i+1

In_2 = browser.find_element_by_xpath("/html/body/center/div/a[2]")
lab_m= browser.find_element_by_link_text('lab@cs.ccu.edu.tw')
print(lab_m.get_attribute("href")) #有問題的mail
i=i+1
In_3 = browser.find_element_by_xpath("/html/body/center/div/a[3]")
office_m= browser.find_element_by_link_text('office@cs.ccu.edu.tw')
print(office_m.get_attribute("href")) #行政問題的mail
i=i+1

In_4 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]/a[2]") # 點選 系所成員 頁 
span_m = browser.find_element_by_tag_name('span').click()
span_m_T = browser.find_element_by_css_selector("div[class='quicklink']") # 前往 師資陣容 頁
span_T = browser.find_elements_by_partial_link_text('師資陣容')[0].click() #點選 師資陣容 頁

In_5 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]")#QQQ
Teacher_m=browser.find_elements_by_xpath('.//td[contains(text(), "E-mail:")]')
#at=browser.find_elements_by_xpath('.//td[contains(text(), "E-mail:")]/img')
count_1=0
for a in Teacher_m:
    b="@ccu.edu.tw"
    a=a.text
    a=a.replace("E-mail:","")
    a=a[0:-13]
    mail_dict[i]=a+b
    print(a+b)
    i=i+1
    count_1=count_1+1


i=i+count_1
browser.execute_script("window.history.go(-1)")

In_6 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]/a[2]") # 點選 系所成員 頁 
span_m = browser.find_element_by_tag_name('span').click()
span_m_T = browser.find_element_by_css_selector("div[class='quicklink']") # 前往 學生成員 頁
span_T = browser.find_elements_by_partial_link_text('學生成員')[0].click() #點選 學生成員 頁
browser.execute_script("window.history.go(-1)")

In_7 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]/a[2]") # 點選 系所成員 頁 
span_m = browser.find_element_by_tag_name('span').click()
span_m_T = browser.find_element_by_css_selector("div[class='quicklink']") # 前往 系辦成員 頁
span_T = browser.find_elements_by_partial_link_text('系辦成員')[0].click() #點選 系辦成員 頁
In_9 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[3]/td/table[2]/tbody/tr/td/table/tbody")
Member_1=browser.find_elements_by_xpath('.//tr[2]/td/a')[1]
print(Member_1.get_attribute('href'))
i=i+1
Member_2=browser.find_elements_by_xpath('.//tr[3]/td/a')[0]
print(Member_2.get_attribute('href'))
i=i+1
Member_3=browser.find_elements_by_xpath('.//tr[4]/td/a')[0]
print(Member_3.get_attribute('href'))
i=i+1
Member_4=browser.find_elements_by_xpath('.//tr[5]/td/a')[0]
print(Member_4.get_attribute('href'))
i=i+1
browser.execute_script("window.history.go(-1)")
In_13 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]") # 點選 修業資訊 頁 
span_m_T = browser.find_element_by_css_selector("div[class='quicklink']") # 前往 修業資訊 頁
span_T = browser.find_elements_by_partial_link_text('修業資訊')[0].click() #點選 修業資訊 頁
browser.execute_script("window.history.go(-1)")

span_T = browser.find_elements_by_partial_link_text('招生資訊')[0].click() #點選 招生資訊 頁
browser.execute_script("window.history.go(-1)")

span_T = browser.find_elements_by_partial_link_text('表單下載')[0].click() #點選 表單下載 頁
browser.execute_script("window.history.go(-1)")

span_T = browser.find_elements_by_partial_link_text('公告事項')[0].click() #點選 公告事項 頁
browser.execute_script("window.history.go(-1)")

In_14 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]") # 點選 獎學金專區 頁 
span_T = browser.find_elements_by_partial_link_text('獎學金專區')[0].click() #點選 獎學金專區 頁
browser.execute_script("window.history.go(-1)")

In_15 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]/a[8]") # 點選 新聞專區 頁 
span_m = browser.find_element_by_tag_name('span').click()
span_m_T = browser.find_element_by_css_selector("div[class='quicklink']") 
span_T =browser.find_element_by_tag_name('a').click()#點選 媒體報導 頁
browser.execute_script("window.history.go(-1)")

In_16 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]/div[2]") # 點選 新聞專區 頁 
span_m = browser.find_element_by_tag_name('span').click()
span_m_T = browser.find_element_by_css_selector("div[id='sub5']") # 前往 新聞專區 頁
span_T =browser.find_element_by_tag_name('a') #點選 中正首頁新聞 頁
browser.execute_script("window.history.go(-1)")

In_17 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]/div[2]") # 點選 新聞專區 頁 
span_m = browser.find_element_by_tag_name('span').click()
span_m_T = browser.find_element_by_css_selector("div[class='quicklink']") # 前往 新聞專區 頁
span_T =browser.find_element_by_tag_name('a') #點選 中正資工電子報 頁
browser.execute_script("window.history.go(-1)")

In_18 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]/a[9]") # 點選 IEET工程認證 頁 
span_m = browser.find_element_by_tag_name('span').click()
span_m_T = browser.find_element_by_css_selector("div[class='quicklink']") # 前往 IEET工程認證 頁
span_T = browser.find_elements_by_partial_link_text('IEET工程認證')[0].click() #點選 IEET工程認證 頁
browser.execute_script("window.history.go(-1)")



In_23 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]/div[4]") # 點選 相關學程 頁 
span_T = browser.find_elements_by_partial_link_text('系友專區')[0].click() #點選 系友專區 頁
browser.execute_script("window.history.go(-1)")

In_10 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/div[1]/a[2]") # 點選 實驗室 頁 
span_m = browser.find_element_by_tag_name('span').click()
span_m_T = browser.find_element_by_css_selector("div[class='quicklink']") # 前往 實驗室 頁
span_T = browser.find_elements_by_partial_link_text('實驗室')[0].click() #點選 實驗室 頁

In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_1=browser.find_elements_by_xpath('.//tr[4]/td[2]')[1]
span_T = browser.find_elements_by_partial_link_text('應用計算實驗室')[0] #得到 應用計算實驗室 頁
browser.window_handles[0]=browser.get("http://140.123.102.14:8080/home/")
count_2=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/center/table[4]/tbody/tr/td[2]/div/a")
    browser.find_elements_by_partial_link_text('ACL 成員')[0].click()
    browser.find_element_by_xpath("/html/body/center/table[7]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[2]")
    ACL_1=browser.find_elements_by_xpath('.//td/a')
    #rt=ACL_1.get_attribute('href')
    for rt in ACL_1:
     count_2=count_2+1
     print(rt.text)
     i=i+1
    browser.find_element_by_xpath("/html/body/center/table[5]/tbody/tr/td[3]/div/a")
    browser.find_elements_by_partial_link_text('畢業學長')[0].click()
    browser.find_element_by_xpath("/html/body/center/table[7]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]")   
    ACL_2=browser.find_elements_by_xpath('.//td/p/font/a')
    for rt in ACL_2:
     count_2=count_2+1
     print(rt.text)
     i=i+1
    browser.find_element_by_xpath("/html/body/center/table[7]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[30]")   
    ACL_3=browser.find_elements_by_xpath('.//td/font/a')
    for rt in ACL_3:
     count_2=count_2+1
     print(rt.text)
     i=i+1
    browser.find_element_by_xpath("/html/body/center/table[5]/tbody/tr/td[8]/div/a")
    browser.find_elements_by_partial_link_text('專題生')[0].click()
    browser.find_element_by_xpath("/html/body/center/table[7]/tbody/tr/td/table/tbody/tr/td/div[2]/table/tbody/tr[2]")      
    ACL_4=browser.find_elements_by_xpath('.//td[2]/a')
    for rt in ACL_4:
     count_2=count_2+1
     print(rt.text)
     i=i+1    

i=i+count_2
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")

Lab_2=browser.find_elements_by_xpath('.//tr[5]/td[2]')
span_T = browser.find_elements_by_partial_link_text('程式語言實驗室')[0] #點選 程式語言實驗室 頁
browser.window_handles[0]=browser.get("http://www.cs.ccu.edu.tw/~naiwei/")
count_3=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/ul[4]/li/h3/a")
    browser.find_elements_by_partial_link_text('CS1005 - Introduction to Computer Science (I)')[0].click()
    browser.find_element_by_xpath("/html/body/table[2]/tbody/tr/td")
    P_1=browser.find_elements_by_xpath('.//td/a[1]')
    #rt=ACL_1.get_attribute('href')
    for rt in P_1:
     count_3=count_3+1
     print(rt.text)
     i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[2]/h3/a")
    browser.find_elements_by_partial_link_text('CS1006 - Introduction to Computer Science (II)')[0].click()
    browser.find_element_by_xpath("/html/body/table[2]/tbody/tr/td")
    P_2=browser.find_elements_by_xpath('.//td/a[1]')
    #rt=ACL_1.get_attribute('href')
    for rt in P_2:
     count_3=count_3+1
     print(rt.text)
     i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[3]/h3/a")
    browser.find_elements_by_partial_link_text('CS2160 - Object-Oriented Programming')[0].click()
    browser.find_element_by_xpath("/html/body/ul")
    P_3=browser.find_elements_by_xpath('.//li/a[1]')    
    #rt=ACL_1.get_attribute('href')
    for rt in P_3:
     if("hotmail" in rt.text ):
      count_3=count_3+1
      print(rt.text)
     i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[4]/h3/a")
    browser.find_elements_by_partial_link_text('CS3020 - Introduction to Programming Languages')[0].click()
    browser.find_element_by_xpath("/html/body")
    P_4=browser.find_elements_by_xpath('.//a')
    #rt=ACL_1.get_attribute('href')
    for rt in P_4:
     if("@" in rt.text ):
      count_3=count_3+1
      print(rt.text)
      i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[5]/h3/a")
    browser.find_elements_by_partial_link_text('CS3021 - Software Quality Management')[0].click()
    browser.find_element_by_xpath("/html/body")
    P_5=browser.find_elements_by_xpath('.//a')
    #rt=ACL_1.get_attribute('href')
    for rt in P_5:
     if("@" in rt.text ):
      count_3=count_3+1
      print(rt.text)
      i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[6]/h3/a")
    browser.find_elements_by_partial_link_text('CS4005 - Compiler Design')[0].click()
    browser.find_element_by_xpath("/html/body")
    P_6=browser.find_elements_by_xpath('.//a')
    #rt=ACL_1.get_attribute('href')
    for rt in P_6:
     if("@" in rt.text ):
      count_3=count_3+1
      print(rt.text)
      i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[7]/h3/a")
    browser.find_elements_by_partial_link_text('CS5605 - Compilers')[0].click()
    browser.find_element_by_xpath("/html/body")
    P_7=browser.find_elements_by_xpath('.//a')
    #rt=ACL_1.get_attribute('href')
    for rt in P_7:
     if("@" in rt.text ):
      count_3=count_3+1
      print(rt.text)
      i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[8]/h3/a")
    browser.find_elements_by_partial_link_text('CS5610 - Advanced Compilers')[0].click()
    browser.find_element_by_xpath("/html/body")
    P_8=browser.find_elements_by_xpath('.//a')
    #rt=ACL_1.get_attribute('href')
    for rt in P_8:
     if("@" in rt.text ):
      count_3=count_3+1
      print(rt.text)
      i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[9]/h3/a")
    browser.find_elements_by_partial_link_text('CS5630 - Programming Languages')[0].click()
    browser.find_element_by_xpath("/html/body")
    P_9=browser.find_elements_by_xpath('.//a')
    #rt=ACL_1.get_attribute('href')
    for rt in P_9:
     if("@" in rt.text ):
      count_3=count_3+1
      print(rt.text)
      i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[10]/h3/a")
    browser.find_elements_by_partial_link_text('CS5635 - Parallel Programming')[0].click()
    browser.find_element_by_xpath("/html/body")
    P_10=browser.find_elements_by_xpath('.//a')
    #rt=ACL_1.get_attribute('href')
    for rt in P_10:
     if("@" in rt.text ):
      count_3=count_3+1
      print(rt.text)
      i=i+1
    browser.execute_script("window.history.go(-1)")
    browser.find_element_by_xpath("/html/body/ul[4]/li[11]/h3/a")
    browser.find_elements_by_partial_link_text('CS5812 - Software Testing')[0].click()
    browser.find_element_by_xpath("/html/body")
    P_11=browser.find_elements_by_xpath('.//a')
    #rt=ACL_1.get_attribute('href')
    for rt in P_11:
     if("@" in rt.text ):
      count_3=count_3+1
      print(rt.text)
      i=i+1
i=i+count_3
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")

Lab_3=browser.find_elements_by_xpath('.//tr[6]/td[2]')
span_T = browser.find_elements_by_partial_link_text('系統軟體實驗室')[0] #點選 系統軟體實驗室 頁
browser.window_handles[0]=browser.get("http://140.123.102.237:301/")
count_4=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/div/div[2]/ul/li[2]")
    browser.find_elements_by_partial_link_text('系統軟體實驗室')[0].click()

browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")


#Lab_4=browser.find_elements_by_xpath('.//tr[7]/td[2]')[1]
#span_T = browser.find_elements_by_partial_link_text('電腦遊戲人工智能與資料探勘實驗室')[0] #點選 電腦遊戲人工智能與資料探勘實驗室 頁 #壞掉

In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_5=browser.find_elements_by_xpath('.//tr[8]/td[2]')[0]
span_T = browser.find_elements_by_partial_link_text('多媒體運算實驗室')[0] #點選 多媒體運算實驗室 頁
browser.window_handles[0]=browser.get("http://mclab.cs.ccu.edu.tw/")
count_6=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/div/nav/div/ul/li[2]")
    browser.find_elements_by_partial_link_text('Member')[0].click()
    browser.find_element_by_xpath("/html/body/div/div[3]/div[2]/div/div[2]/ul")
    M_1=browser.find_elements_by_xpath('.//li[2]')
    #rt=ACL_1.get_attribute('href')
    for rt in M_1:
     count_6=count_6+1
     rt=rt.text
     rt=rt.replace("Email:","")
     print(rt)
     i=i+1

browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")
"""
#要改
In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_6=browser.find_elements_by_xpath('.//tr[9]/td[2]')
span_T = browser.find_elements_by_partial_link_text('資料管理實驗室')[0] #點選 資料管理實驗室 頁
browser.window_handles[0]=browser.get("http://dmplus.cs.ccu.edu.tw/")
count_7=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/ul/li[2]")
    browser.get("http://140.123.102.98/wordpress_dmplus/?page_id=21")
    browser.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div/div/div/div/div/div/table/tbody")
    D_1=browser.find_elements_by_xpath('.//tr/td') #有br 的問題
    for rt in D_1:
     count_7=count_7+1
     rt=rt.text
     mail_dict[i]=rt
     print(rt)
     i=i+1
i=i+count_7
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")
"""
#In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_7=browser.find_elements_by_xpath('.//tr[10]/td[2]')
span_T = browser.find_elements_by_partial_link_text('作業系統實驗室')[0] #點選 作業系統實驗室 頁
browser.window_handles[0]=browser.get("http://osl.cs.ccu.edu.tw")
count_8=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/div/div/ul/li[4]/a")
    browser.find_elements_by_partial_link_text('聯絡我們')[0].click()
    browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/p[3]")
    OS_m = browser.find_elements_by_partial_link_text('ccu.oslab.sa@outlook.com')[0]
    OS_1=OS_m.get_attribute("href") 
    OS_1=OS_1.replace("mailto:","")
    print(OS_1)
i=i+1
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")  

#In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
#Lab_8=browser.find_elements_by_xpath('.//tr[11]/td[2]')
#span_T = browser.find_elements_by_partial_link_text('影像處理暨電腦視覺實驗室')[0] #點選 影像處理暨電腦視覺實驗室 頁
#browser.window_handles[0]=browser.get("http://donald.cs.ccu.edu.tw/") #壞掉


In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_9=browser.find_elements_by_xpath('.//tr[12]/td[2]')
span_T = browser.find_elements_by_partial_link_text('計算視覺與認知實驗室')[0] #點選 計算視覺與認知實驗室 頁
browser.window_handles[0]=browser.get("http://140.123.102.5:8090/") 
count_9=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/header/nav/ul/li[2]/a")
    browser.find_elements_by_partial_link_text('研究室成員')[0].click()
    browser.find_element_by_xpath("/html/body/div/div/section[2]")
    CC_1=browser.find_elements_by_xpath('.//div/p[3]') #有br 的問題
    for rt in CC_1:
     count_9=count_9+1
     rt=rt.text
     rt=rt.replace("Email:","")
     print(rt)
     i=i+1
i=i+count_9
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")
browser.get("https://www.cs.ccu.edu.tw/resource/resource.php")

#In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
#Lab_10=browser.find_elements_by_xpath('.//tr[13]/td[2]')
#span_T = browser.find_elements_by_partial_link_text('行動計算與網路實驗室') #點選 行動計算與網路實驗室 頁
#browser.window_handles[0]=browser.get("http://donald.cs.ccu.edu.tw/") #用firefox無法開


In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_11=browser.find_elements_by_xpath('.//tr[14]/td[2]')
span_T = browser.find_elements_by_partial_link_text('高速網路與多媒體網路實驗室')[0] #點選 高速網路與多媒體網路實驗室 頁
browser.window_handles[0]=browser.get("http://exodus.cs.ccu.edu.tw/") 
count_11=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
browser.execute_script("window.history.go(-1)")

#In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
#Lab_12=browser.find_elements_by_xpath('.//tr[15]/td[2]')
#span_T = browser.find_elements_by_partial_link_text('模糊理論與類神經網路實驗室')[0] #點選 模糊理論與類神經網路實驗室 頁
#browser.window_handles[0]=browser.get("http://neuralpc1.cs.ccu.edu.tw/") #無法開


In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_13=browser.find_elements_by_xpath('.//tr[16]/td[2]')
span_T = browser.find_elements_by_partial_link_text('社會網路分析實驗室')[0] #點選 社會網路分析實驗室 頁
browser.window_handles[0]=browser.get("http://sna.cs.ccu.edu.tw/") 
count_13=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.get("http://sna.cs.ccu.edu.tw/member.html") 
    browser.find_element_by_xpath("/html/body/div/div[4]/div/div[3]")
    SA_1=browser.find_elements_by_xpath('.//div/p/a') 
    for rt in SA_1:
     if("@" in rt.text or "＠" in rt.text):
      count_13=count_13+1
      rt=rt.text
      rt=rt.replace("Email:","")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")

In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_14=browser.find_elements_by_xpath('.//tr[17]/td[2]')
span_T = browser.find_elements_by_partial_link_text('網路與系統安全實驗室')[0] #點選 網路與系統安全實驗室 頁
browser.window_handles[0]=browser.get("https://www.cs.ccu.edu.tw/~pclin/lab.html") 
count_14=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.get("https://www.cs.ccu.edu.tw/~pclin/index2.html")
    browser.get("https://www.cs.ccu.edu.tw/~pclin/members.html")
    browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody")
    SA_1=browser.find_elements_by_xpath('.//tr/td') 
    for rt in SA_1:
     if(" AT " in rt.text):
      count_14=count_14+1
      rt=rt.text
      rt=rt.replace(" AT ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1

i=i+count_14
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")
""""""

##In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_15=browser.find_elements_by_xpath('.//tr[18]/td[2]')
span_T = browser.find_elements_by_partial_link_text('生物資訊實驗室')[0] #點選 生物資訊實驗室 頁
browser.window_handles[0]=browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/") 
count_15=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/grad105.php") 
    browser.find_element_by_xpath("/html/body/div/div/div[2]")
    BA_1=browser.find_elements_by_xpath('.//p/a') 
    for rt in BA_1:
     if(" at " in rt.text):
      count_15=count_15+1
      rt=rt.text
      rt=rt.replace(" at ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1
    browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/grad104.php") 
    browser.find_element_by_xpath("/html/body/div/div/div[2]")
    BA_1=browser.find_elements_by_xpath('.//p/a') 
    for rt in BA_1:
     if(" at " in rt.text):
      count_15=count_15+1
      rt=rt.text
      rt=rt.replace(" at ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1
    browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/grad103.php") 
    browser.find_element_by_xpath("/html/body/div/div/div[2]")
    BA_1=browser.find_elements_by_xpath('.//p/a') 
    for rt in BA_1:
     if(" at " in rt.text):
      count_15=count_15+1
      rt=rt.text
      rt=rt.replace(" at ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1
    browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/grad102.php") 
    browser.find_element_by_xpath("/html/body/div/div/div[2]")
    BA_1=browser.find_elements_by_xpath('.//p/a') 
    for rt in BA_1:
     if(" at " in rt.text):
      count_15=count_15+1
      rt=rt.text
      rt=rt.replace(" at ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1
    browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/grad101.php") 
    browser.find_element_by_xpath("/html/body/div/div/div[2]")
    BA_1=browser.find_elements_by_xpath('.//p/a') 
    for rt in BA_1:
     if(" at " in rt.text):
      count_15=count_15+1
      rt=rt.text
      rt=rt.replace(" at ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1
    browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/grad100.php") 
    browser.find_element_by_xpath("/html/body/div/div/div[2]")
    BA_1=browser.find_elements_by_xpath('.//p/a') 
    for rt in BA_1:
     if(" at " in rt.text):
      count_15=count_15+1
      rt=rt.text
      rt=rt.replace(" at ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1
    browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/grad99.php") 
    browser.find_element_by_xpath("/html/body/div/div/div[2]")
    BA_1=browser.find_elements_by_xpath('.//p/a') 
    for rt in BA_1:
     if(" at " in rt.text):
      count_15=count_15+1
      rt=rt.text
      rt=rt.replace(" at ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1
    browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/grad98.php") 
    browser.find_element_by_xpath("/html/body/div/div/div[2]")
    BA_1=browser.find_elements_by_xpath('.//p/a') 
    for rt in BA_1:
     if(" at " in rt.text):
      count_15=count_15+1
      rt=rt.text
      rt=rt.replace(" at ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1
    browser.get("http://bioinfo.cs.ccu.edu.tw/bioinfo/grad97.php") 
    browser.find_element_by_xpath("/html/body/div/div/div[2]")
    BA_1=browser.find_elements_by_xpath('.//p/a') 
    for rt in BA_1:
     if(" at " in rt.text):
      count_15=count_15+1
      rt=rt.text
      rt=rt.replace(" at ","@")
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1

i=i+count_15
browser.get("https://www.cs.ccu.edu.tw/resource/resource.php")

#要再看看
Lab_16=browser.find_elements_by_xpath('.//tr[19]/td[2]')
span_T = browser.find_elements_by_partial_link_text('矽感測器與系統實驗室')[0] #點選 矽感測器與系統實驗室 頁
browser.window_handles[0]=browser.get("https://www.cs.ccu.edu.tw/~wildwolf/") 
count_16=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.get("http://www.cs.ccu.edu.tw/~wildwolf/S3LAB.html") 
    browser.find_element_by_xpath("/html/body/div/div/table/tbody/tr")
    Si_1=browser.find_elements_by_xpath('./td[3]/p/span') 
    for rt in Si_1:
     if(" AT " in rt.text):
      count_16=count_16+1
      mail_dict[i]=rt[:3]
      print(rt)
      i=i+1

i=i+count_16
"""
Lab_18=browser.find_elements_by_xpath('.//tr[21]/td[2]')
span_T = browser.find_elements_by_partial_link_text('行動網路通訊實驗室')[0] #點選 行動網路通訊實驗室 頁
browser.window_handles[0]=browser.get("http://mainlab.cs.ccu.edu.tw/") 
count_18=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/header/div/nav/div/ul/li[2]/a")
    browser.find_elements_by_partial_link_text('研究成員')[0].click()
    browser.find_element_by_xpath("/html/body/section/div/div[5]/div/table/tbody")#麻煩的==
    MN_1=browser.find_elements_by_xpath('.//tr/td[3]') 
    for rt in MN_1:
      count_18=count_18+1
      mail_dict[i]=rt.text
      print(rt.text)
      i=i+1

i=i+count_18
"""



#In_11 = browser.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody")
Lab_19=browser.find_elements_by_xpath('.//tr[22]/td[2]')
#span_T = browser.find_elements_by_partial_link_text('創新計算系統與視覺化科技實驗室')[0] 
#browser.window_handles[0]=browser.get("http://140.123.101.97/") #點選 創新計算系統與視覺化科技實驗室 頁
#count_19=0
#for handle in browser.window_handles:
    #browser.switch_to.window(handle)
#i=i+count_19
#browser.get("https://www.cs.ccu.edu.tw/resource/resource.php")

#Lab_20=browser.find_elements_by_xpath('.//tr[23]/td[2]')[1]#壞掉
#span_T = browser.find_elements_by_partial_link_text('GAIS實驗室')[0] #點選 GAIS實驗室 頁 



#Lab_21=browser.find_elements_by_xpath('.//tr[24]/td[2]')
#span_T = browser.find_elements_by_partial_link_text('嵌入式系統實驗室')[0] #點選 嵌入式系統實驗室 頁
#browser.window_handles[0]=browser.get("http://embedded.cs.ccu.edu.tw/") #點選 創新計算系統與視覺化科技實驗室 頁
#browser.execute_script("window.history.go(-1)")
"""
Lab_22=browser.find_elements_by_xpath('.//tr[25]/td[2]')
span_T = browser.find_elements_by_partial_link_text('計算型智慧實驗室')[0] #點選 計算型智慧實驗室 頁
browser.window_handles[0]=browser.get("http://cilab.cs.ccu.edu.tw/")
count_22=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.get("http://cilab.cs.ccu.edu.tw/lab_memb.html")#壞掉
i=i+count_22
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")
"""
Lab_23=browser.find_elements_by_xpath('.//tr[26]/td[2]')
#span_T = browser.find_elements_by_partial_link_text('高效能計算實驗室(HPC Lab)') #點選 高效能計算實驗室(HPC Lab) 頁
browser.window_handles[0]=browser.get("http://hpcweb.cs.ccu.edu.tw/")
count_23=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/div/ul/li[2]/span/a")
    browser.find_elements_by_partial_link_text('Members')[0].click()
    browser.find_element_by_xpath("/html/body/div/table/tbody")
    HC_1=browser.find_elements_by_xpath('.//tr/td[3]/div/font') 
    for rt in HC_1:
      count_23=count_23+1
      mail_dict[i]=rt.text
      print(rt.text)
      i=i+1
print(count_23)
i=i+count_23
print(i)
browser.get("https://www.cs.ccu.edu.tw/index2.php")

"""
Lab_24=browser.find_elements_by_xpath('.//tr[27]/td[2]')
span_T = browser.find_elements_by_partial_link_text('醫學與遙測影像實驗室')[0] #點選 醫學與遙測影像實驗室 頁
browser.window_handles[0]=browser.get("https://www.cs.ccu.edu.tw/~wmliu/")
count_24=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr/td[3]/a")
    browser.find_elements_by_partial_link_text('Members')[0].click()
    #browser.find_element_by_xpath("/html/body/div/table/tbody")#麻煩的==
    #MR_1=browser.find_elements_by_xpath('.//tr/td[3]/div/font')
    for rt in MR_1:
      count_24=count_24+1
      mail_dict[i]=rt.text
      print(rt.text)
      i=i+1
print(count_24)
i=i+count_24
print(i)
#browser.execute_script("window.history.go(-1)")
#browser.execute_script("window.history.go(-1)")

#要改的
Lab_25=browser.find_elements_by_xpath('.//tr[28]/td[2]')
span_T = browser.find_elements_by_partial_link_text('機器視覺學習實驗室')[0] #點選 機器視覺學習實驗室 頁
browser.window_handles[0]=browser.get("http://mvllab.cs.ccu.edu.tw/")
count_25=0
for handle in browser.window_handles:
    browser.switch_to.window(handle)
    browser.get("http://mvllab.cs.ccu.edu.tw/members.html")
    browser.find_element_by_xpath("/html/body/div/div[4]/div/div/div/div/div")#麻煩的==
    MS_1=browser.find_elements_by_xpath('.//table/tbody/tr/td/p[2]')
    for rt in MS_1:
      count_25=count_25+1
      rt=rt.text
      rt=rt.replace("Email: ","")
      mail_dict[i]=rt
      print(rt)
      i=i+1
print(count_25)
i=i+count_25
print(i)
browser.execute_script("window.history.go(-1)")
browser.execute_script("window.history.go(-1)")
"""




