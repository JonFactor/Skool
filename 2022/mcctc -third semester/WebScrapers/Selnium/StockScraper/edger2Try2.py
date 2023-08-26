#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def finds(x , method = 'X', multiple = False, parent = None ,t = 5):
    try:
        if method == 'X':
            WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.XPATH, x)))
            if parent == None:
                if not multiple: return driver.find_element(By.XPATH, x)
                else: return driver.find_elements(By.XPATH, x)
            else:
                if not multiple: return driver.find_element(By.XPATH, x)
                else: return parent.find_elements(By.XPATH, x)
        elif method == 'T':
            WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.TAG_NAME, x)))
            if parent == None:
                if not multiple: return driver.find_element(By.TAG_NAME, x)
                else: return driver.find_elements(By.TAG_NAME, x)
            else:
                if not multiple: return driver.find_element(By.TAG_NAME, x)
                else: return parent.find_elements(By.TAG_NAME, x)
        elif method == 'C':
            WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.CLASS_NAME, x)))
            if parent == None:
                if not multiple: return driver.find_element(By.CLASS_NAME, x)
                else: return driver.find_elements(By.CLASS_NAME, x)
            else:
                if not multiple: return driver.find_element(By.CLASS_NAME, x)
                else: return parent.find_elements(By.CLASS_NAME, x)
    except Exception:
        return None

# import
tickers = []
contents = []
for filename in os.listdir('WebScrapers\Selnium\StockScraper\data'):
    f = os.path.join('WebScrapers\Selnium\StockScraper\data', filename)
    with open(f, 'r') as reading:
        fJson = json.load(reading)
    tickers.append(filename.strip('.json'))
    if fJson == []: contents.append('null')
    else: contents.append(fJson)
# get data
x = 0 # counter
# set keys
key = '1422142'
driver = webdriver.Chrome('C:\\Users\Factor_Jon\Desktop\chromedriver.exe') # start setelnium
for tick in tickers:
    tickData = []
    while x < len(contents):
        linkData = []
        while True:
            content = contents[x]
            if content == 'null': 
                x += 1
                break
            else: pass
            for link in content:  
                link = link.replace('-', '')
                if link[-2:] == '/x': link = link + 'slF345X03/doc4.xml'
                elif link[-9:] == 'ment1.htm': link = link[:-9] + 'xslF345X03/doc4.xml'
                try:
                    driver.get('https://www.sec.gov/Archives/edgar/data/'+key+'/'+link)
                    # get data
                    datas = finds('FormData', 'C', True, t = .1)
                    data2s = []
                    for data in datas:
                        data2s.append(data.text)
                    linkData.append(data2s)
                except Exception: pass
    tickData.append(linkData)   
    with open('WebScrapers\Selnium\StockScraper\data2\[' + tick + '].json', 'w') as write:
        json.dump(tickData , write)
    # last
    x += 1