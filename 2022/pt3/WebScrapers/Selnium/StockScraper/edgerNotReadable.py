
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    if finds('//*[@id="no-results-grid"]/div/h4', .1) == None: y = True
    else: y = False
tickers = open('WebScrapers\Selnium\StockScraper\\refined.json', 'r').read().split(',')[1:]
driver = webdriver.Chrome('C:\\Users\Factor_Jon\Desktop\chromedriver.exe')
for tick in tickers:
    x = 2
    forms=[]
    driver.get(f'https://www.sec.gov/edgar/search/#/q=' + tick[1:].replace("\"", '') + '&category=form-cat2&filter_forms=4')
    y = True
    checkEmpty()
    while y:
        try:
            for tr in finds('//*[@id="hits"]/table/tbody', 1).find_elements(By.TAG_NAME, 'tr'):
                if not tr.find_element(By.TAG_NAME, 'a').get_attribute('data-adsh') + '/'  + tr.find_element(By.TAG_NAME, 'a').get_attribute('href').strip('https://www.sec.gov/edgar/search/#') in forms:
                    if 'doc4.xml' in tr.find_element(By.TAG_NAME, 'a').get_attribute('href'):
                        forms.append(tr.find_element(By.TAG_NAME, 'a').get_attribute('data-adsh') + '/'  + tr.find_element(By.TAG_NAME, 'a').get_attribute('href').strip('https://www.sec.gov/edgar/search/#'))
                else:
                    pass
            driver.get(f'https://www.sec.gov/edgar/search/#/q=' + tick[1:].replace("\"", '') + '&category=form-cat2&filter_forms=4' + f'&page={x}')
            x += 1
            checkEmpty()
        except Exception:
            break
    with open('WebScrapers\Selnium\StockScraper\data\['+tick[1:].replace("\"", '')+'].json', 'w') as a:
        json.dump(forms,a)
driver.quit()