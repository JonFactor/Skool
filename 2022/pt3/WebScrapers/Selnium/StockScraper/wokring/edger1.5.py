#https://www.sec.gov/cgi-bin/browse-edgar?CIK=
from selenium import webdriver
from selenium.webdriver.common.by import By
import json, os, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('WebScrapers\Selnium\StockScraper\\refined.json', 'r') as read:
    tickers = json.load(read)

driver = webdriver.Chrome('C:\\Users\Factor_Jon\Desktop\chromedriver.exe')
ciks = []
for ticker in tickers:
    driver.get('https://www.sec.gov/cgi-bin/browse-edgar?CIK='+ticker)
    try:
        WebDriverWait(driver, .1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="contentDiv"]/div[1]/div[3]/span/a')))
        ciks.append(driver.find_element(By.XPATH, '//*[@id="contentDiv"]/div[1]/div[3]/span/a').text.strip(' (see all company filings)'))
    except Exception: 
        ciks.append('NAHHHHHHHHHH')
        pass
driver.quit()

with open('WebScrapers\Selnium\StockScraper\ciks.json', 'w') as write:
    json.dump(ciks, write)