
############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path 
import os 
import re 
import json, random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
############### Defining ###############
def findsclick(x, t = 5):
    try:
        WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).click()
    except Exception:
        pass
def findsEntry(x, y, t = 5):
    try:
        WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).send_keys(y, Keys.ENTER)   
    except Exception:
        pass
def finds(x , t = 5):
    try:
        WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.XPATH, x)))
        return driver.find_element(By.XPATH, x)
    except Exception:
        return None
def checkEmpty():
    global y
    d = finds('//*[@id="no-results-grid"]/div/h4', 1)
    if d == None: y = True
    else: y = False
#PATH = "C:\Program Files (x86)\chromedriver.exe"# Home

driver = webdriver.Chrome('C:\\Users\Factor_Jon\Desktop\chromedriver.exe')
# tickers
with open('WebScrapers\Selnium\StockScraper\\refined.json', 'r') as r:
    tickers = r.read()
    tickers = tickers.split(',')[1:]

for tick in tickers:
    x = 2
    forms=[]
    refinedTick = tick[1:].strip("\"")
    link = f'https://www.sec.gov/edgar/search/#/q=' + refinedTick + '&category=form-cat2&filter_forms=4'
    driver.get(link)
    y = True
    # setting
    checkEmpty()
    while y:
        try:
            # 2
            fourmtable = finds('//*[@id="hits"]/table/tbody')
            tableTrs = fourmtable.find_elements(By.TAG_NAME, 'tr')
            for tr in tableTrs:
                type4 = tr.find_element(By.CLASS_NAME, 'filetype')
                # get data shit
                a = tr.find_element(By.TAG_NAME, 'a')
                adsh = a.get_attribute('data-adsh')
                href = a.get_attribute('href').strip('https://www.sec.gov/edgar/search/#')
                combine = a.get_attribute('data-adsh') + '/'  + a.get_attribute('href').strip('https://www.sec.gov/edgar/search/#')
                if not combine in forms:
                    forms.append(combine)
                else:
                    pass
    
            #--->
            driver.get(link + f'&page={x}')
            x += 1
            checkEmpty()

        except Exception:
            pass
    # save data
    with open(f'WebScrapers\Selnium\StockScraper\data\[{refinedTick}].json', 'w') as file:
        json.dump(forms,file)
    print(1)
driver.quit()