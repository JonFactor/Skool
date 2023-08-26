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
with open('WebScrapers\Selnium\StockScraper\ciks.json', 'r') as read:
    ciks = json.load(read)
print(len(ciks))
Z = True
# start
driver = webdriver.Chrome("D:\CodeShit\chromedriver_win32\chromedriver.exe")
ALLdata = []
counter = 0
while counter > 4660:
    CIKdata = []
    driver.get(f'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={ciks[counter]}&type=4&dateb=&owner=include&count=100&search_text=')
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
                table2 = finds('table', True, True,driver, 1)
                trs = finds('tr', True, True, table2[0], 1)
                tds = finds('td', True, True, trs[1], 1)
                data = []
                tds[2].find_element(By.TAG_NAME, 'a').click()
                data.append(finds('/html/body/table[2]/tbody/tr[1]/td[1]/table[1]/tbody/tr/td/a', t=1).text)
                try: data.append(finds('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[1]/td[1]/span', t=.1).text)
                except Exception: data.append(0)
                try: data.append(finds('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[1]/td[3]/span', t=.1).text)
                except Exception: data.append(0)
                try: data.append(finds('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[2]/td[1]/span', t=.1).text)
                except Exception: data.append(0)
                x = 1
                if finds('/html/body/table[3]/tbody/tr') == None:
                    while True:
                        xData = []
                        y = 1
                        yData = []
                        while y <= 10:
                            if not y == 8:
                                td = finds(f'/html/body/table[3]/tbody/tr[{x}]/td[{y}]/span', t = .5).text
                                if td == None: 
                                    try: td = finds(f'/html/body/table[3]/tbody/tr[{x}]/td[{y}]/span[1]', t = .1)
                                    except Exception: pass
                            else:
                                td = finds(f'/html/body/table[3]/tbody/tr[{x}]/td[{y}]/span[2]', t = .1).text
                            yData.append(td)
                            y += 1
                        xData.append(yData)
                        x += 1
                        CIKdata.append(xData)
                        break
                else:
                    xData = []
                    y = 1
                    while y <= 10:
                        if not y == 8:
                            try:
                                td = finds(f'/html/body/table[3]/tbody/tr/td[{y}]/span', t = .1).text
                            except Exception:
                                try: td = finds(f'/html/body/table[3]/tbody/tr/td[{y}]/span[1]', t = .1)
                                except Exception: pass
                        else:
                            td = finds(f'/html/body/table[3]/tbody/tr/td[{y}]/span[2]', t = .5).text
                        xData.append(td)
                        y += 1
                    CIKdata.append(xData)
            except Exception: driver.back()                    
        except Exception: pass                    
    with open('D:\CodeShit\SEC.Gov\['+ ciks[counter] +'].json','w') as write:
        json.dump(CIKdata, write)
    counter -= 1
driver.quit()
