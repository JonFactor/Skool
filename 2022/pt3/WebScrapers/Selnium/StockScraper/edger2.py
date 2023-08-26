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
keys = ['1422142']
driver = webdriver.Chrome('C:\\Users\Factor_Jon\Desktop\chromedriver.exe') # start setelnium
tickData = []
for tick in tickers:
    linkData = None
    while True:
        content = contents[x]
        if content == 'null': break
        else: pass
        linkData = []
        for link in content:  
            link = link.replace('-', '')
            for key in keys:
                tableData = None
                while True:
                    driver.get('https://www.sec.gov/Archives/edgar/data/'+key+'/'+link)
                    # test if right pg
                    testElement = finds('/html/body/table[1]/tbody/tr[1]/td[2]/span[1]')
                    if testElement == None: break
                    else: pass
                    # get data
                    HTMLbody = finds('body', TAG=True)
                    tables = finds('table', TAG=True, multiple=True,parent=HTMLbody)
                    tableData = []
                    for table in tables:
                        z = True
                        while z:
                            # check 4 right tb
                            THead = finds('thead', True, False, table)
                            if THead == None: z = False
                            HeadTrs = finds('tr', True, True, THead)
                            if len(HeadTrs) != 3: z = False
                            else: pass
                            for tr in HeadTrs:
                                ths = finds('th', True, True, tr)
                                for th in ths:
                                    bs = finds('b', True, True, th)
                                    for b in bs:
                                        if not b.text == 'Table I - Non-Derivative Securities Acquired, Disposed of, or Beneficially Owned': z = False
                                        else: pass
                            # get tb info
                            Tbody = finds('tbody', True, False, table)
                            BodyTrs = finds('tr', True, True, Tbody)
                            trdata = []
                            for tr in BodyTrs:
                                tds = finds('td',True,True,tr)
                                tddata = []
                                for td in tds:
                                    spans = finds('span', True, True, td)
                                    spandata = []
                                    for span in spans:
                                        spandata.append(span.text)
                                    tddata.append(spandata)
                                trdata.append(tddata)
                            tableData.append(trdata)
                            # done
                            break
                linkData.append(tableData)
    tickData.append(linkData)   
    # last
    x += 1