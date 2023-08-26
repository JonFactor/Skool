### importing
## selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
## paths
from pathlib import Path 
## other
import time, os, json, random
import pandas as pd
### varibles
x = 0
### functions
def findsclick(x):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).click()
    except Exception:
        pass
def findsEntry(x, y):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).send_keys(y)
    except Exception:
        pass
def finds(x):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, x)))
        return driver.find_element(By.XPATH, x)
    except Exception:
        return None
### start
driver = webdriver.Chrome()
driver.get('https://clinicaltrials.gov/ct2/show/NCT05702983?cntry=US&draw=2&rank=2')

### set lists

datalist = []
### loop
while True:
    try:
        
        ### get business name
        company = finds('//*[@id="sponsor"]').text
        ### study info
        header = []
        info = []
        findsclick('//*[@id="tabular"]/a')
        time.sleep(.5)
        table = finds('//*[@id="tab-body"]/div[1]/table/tbody')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for tr in rows:
            try:
                tds = tr.find_element(By.TAG_NAME, 'td')
                ths = tr.find_element(By.TAG_NAME, 'th')
                header.append(ths.text)
                info.append(tds.text)
            except Exception:
                pass
        ### check if on correct cite
        if '=' in driver.current_url:
            pass
        else:
            break
        ### organize data
        data = {
            'comany': company,
            'headers': header,
            'info':info
        }
        datalist.append(data)


        ### next pg
        findsclick('//*[@id="search-results"]/div[2]/a[3]')
    except Exception:
        break
driver.close()

### save data
with open('WebScrapers\catalists\data.json', 'w') as outfile:
    json.dump(datalist, outfile, indent=3)

