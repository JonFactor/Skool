from selenium import webdriver
from selenium.webdriver.common.by import By
import json, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
tickers = []
contents = []
for filename in os.listdir('WebScrapers\Selnium\StockScraper\data'):
    f = os.path.join('WebScrapers\Selnium\StockScraper\data', filename)
    with open(f, 'r') as reading:
        fJson = json.load(reading)
    tickers.append(filename.strip('.json'))
    if fJson == []: contents.append('null')
    else: contents.append(fJson)
x = 0 
with open('WebScrapers\Selnium\StockScraper\ciks.json', 'r') as read:
    ciks = json.load(read)
driver = webdriver.Chrome('C:\\Users\Factor_Jon\Desktop\chromedriver.exe')
for tick in tickers:
    tickData = []
    while x < len(contents):
        content = contents[x]
        while True:
            if ciks[x] == 'NAHHHHHHHHHH': 
                x += 1
                break
            if content == 'null': 
                x += 1
                break
            else: pass
            linkData = []
            for link in content:  
                link = link.replace('-', '')
                if link[-2:] == '/x': link = link + 'slF345X03/doc4.xml'
                elif link[-9:] == 'ment1.htm': link = link[:-9] + 'xslF345X03/doc4.xml'
                elif 'f4_a1e2k0000' in link: link = link[:-29] + 'doc4.xml'
                try:
                    driver.get('https://www.sec.gov/Archives/edgar/data/'+str(ciks[x])+'/'+link)
                    data2s = []
                    WebDriverWait(driver, .05).until(EC.visibility_of_element_located((By.CLASS_NAME, 'FormData')))
                    for data in driver.find_elements(By.CLASS_NAME, 'FormData'): data2s.append(data.text)
                    linkData.append(data2s)
                except Exception: pass
            tickData.append(linkData) 
            break
        x += 1  
        with open('WebScrapers\Selnium\StockScraper\data2\[' + tick + '].json', 'w') as w: json.dump(tickData , w)