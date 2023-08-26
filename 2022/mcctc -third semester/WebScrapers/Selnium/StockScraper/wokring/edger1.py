# https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=4&dateb=&owner=include&count=100&search_text=
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def finds(x , TAG = False, multiple = False, parent = None ,t = 5):
    try:
        if not TAG:
            WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.XPATH, x)))
            if parent == None:
                if not multiple: return driver.find_element(By.XPATH, x)
                else: return driver.find_elements(By.XPATH, x)
            else:
                if not multiple: return driver.find_element(By.XPATH, x)
                else: return parent.find_elements(By.XPATH, x)
        else:
            WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.TAG_NAME, x)))
            if parent == None:
                if not multiple: return driver.find_element(By.TAG_NAME, x)
                else: return driver.find_elements(By.TAG_NAME, x)
            else:
                if not multiple: return driver.find_element(By.TAG_NAME, x)
                else: return parent.find_elements(By.TAG_NAME, x)
    except Exception:
        return None
# import
with open('D:\CodeShit\CIKS.json', 'r') as read:
    ciks = json.load(read)
Z = True
# start
driver = webdriver.Chrome('C:\\Users\Factor_Jon\Desktop\chromedriver.exe')
ALLdata = []
for cik in ciks:
    cik = cik[0]
    CIKdata = []
    driver.get(f'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=4&dateb=&owner=include&count=100&search_text=')
    Table = finds('//*[@id="seriesDiv"]/table/tbody', t=1)
    rows = finds('tr', True, True, Table, 1)
    if rows == None: break
    rows2 = []
    for row in rows:
        colunms = finds('td', True, True, row, 1)
        if colunms != None:
            if colunms != []:
                if colunms[0].text == '4': 
                    rows2.append(colunms[1].find_element(By.TAG_NAME, 'a').get_attribute('href'))
    for colunm in rows2:
        try: 
            driver.get(colunm)
            try:
                LinkContain = finds('//*[@id="formDiv"]/div/table/tbody/tr[4]/td[3]')
                LinkContain.find_element(By.PARTIAL_LINK_TEXT, '.txt').click()
                CIKdata.append(finds('pre', True).text)
                driver.back()
                driver.back()
            except Exception: driver.back()                    
        except Exception: pass                    
    with open('D:\CodeShit\SEC.Gov\['+ cik +'].json','w') as write:
        if not CIKdata == [''] or CIKdata == []: json.dump(CIKdata, write)
    pass
driver.quit()
