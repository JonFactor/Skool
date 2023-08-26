############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path 
import os 
import re 
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
############### Defining ###############
def findsclick(x):
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).click()
    except Exception:
        pass
def findsEntry(x, y):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).send_keys(y, Keys.ENTER)   
    except Exception:
        pass
def finds(x):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, x)))
        return driver.find_element(By.XPATH, x)
    except Exception:
        return None
#PATH = "C:\Program Files (x86)\chromedriver.exe"# Home
PATH = 'C:\\Users\Factor_Jon\Desktop\chromedriver.exe'
driver = webdriver.Chrome(PATH)

## running
driver.get('https://www.benzinga.com/sec/insider-trades/search/insider_trading_all')
# body
# popupclose
time.sleep(16)
def btnClickThingy():
    try:
        findsclick('//*[@id="om-pcmctuz83hjqu5f7rfzg-yesno"]/div/button') 
    except Exception:
        try:
            findsclick('//*[@id="om-eidtkvdefc5jjj9uamwy-yesno"]/div/button')
        except Exception:
            try:
                findsclick('//*[@id="om-pr3euwnk3aci7vloznjm-optin"]/div/button')
            except Exception:
                try:
                    findsclick('//*[@id="om-eidtkvdefc5jjj9uamwy-yesno"]/div/button')
                except Exception:
                    try:
                        findsclick('//*[@id="om-eidtkvdefc5jjj9uamwy-yesno"]/div/button')
                    except Exception:
                        findsclick('//*[@id="om-pr3euwnk3aci7vloznjm-optin"]/div/button')
                
    
btnClickThingy()
#go through table
TdValues = []
x = 0
while True:
    # get values
    try:
        Tbody = finds('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div/div/table/tbody[1]')
        TableTrs = Tbody.find_elements(By.TAG_NAME, 'tr')
        for tr in TableTrs:
            RowTds = tr.find_elements(By.TAG_NAME, 'td')
            for td in RowTds:
                TdValues.append(td.text)
    except Exception:
        btnClickThingy()
    # next pg
    findsclick('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div/footer/div/div[2]/div/button[2]')
    # counter
    x += 1
    if x >= 4200:
        break
    else:
        pass
driver.quit()

x = 0
y = 0
indexs = []
tickers = []
names = []
traders = []
titles = []
qty = []
prices = []
sizes = []
filingDates = []
types = []
while x < len(TdValues):
    if y == 0:
        indexs.append(TdValues[x])
        y += 1
    elif y == 1:
        tickers.append(TdValues[x])
        y += 1
    elif y == 2:
        names.append(TdValues[x])
        y += 1
    elif y == 3:
        traders.append(TdValues[x])
        y += 1
    elif y == 4:
        titles.append(TdValues[x])
        y += 1
    elif y == 5:
        qty.append(TdValues[x])
        y += 1
    elif y == 6:
        prices.append(TdValues[x])
        y += 1
    elif y == 7:
        sizes.append(TdValues[x])
        y += 1
    elif y == 8:
        filingDates.append(TdValues[x])
        y += 1
    elif y == 9:
        types.append(TdValues[x])
        y += 1
    elif y >= 10 and y <= 12:
        y +=1
    else:
        y = 0
    x += 1
data = {
    'indexs':indexs,
    'tickers':tickers,
    'names':names,
    'traders':traders,
    'titles':titles,
    'qty':qty,
    'prices':prices,
    'sizes':sizes,
    'filingDates':filingDates,
    'types':types
}
with open('D:\data\\stock.json', 'w') as file:
    json.dump(data, file)
print('done')