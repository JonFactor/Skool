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
### checky varibles
linksA = []
### functions
def findsclick(x):
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).click()
    except Exception:
        pass
def findsEntry(x, y):
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).send_keys(y)
    except Exception:
        pass
### starting
## driver
#PATH = "C:\Program Files (x86)\chromedriver.exe"# Home
PATH = 'C:\\Users\Factor_Jon\Desktop\chromedriver.exe'
driver = webdriver.Chrome(PATH)
## open
driver.get('https://learn.microsoft.com/en-us/docs/')
### body
## pg 1
# get all links for all pages
XlinksUL = '//*[@id="listings-section"]/div/div/ul'
WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, XlinksUL)))
linksUL = driver.find_element(By.XPATH, XlinksUL)
linksLI = linksUL.find_elements(By.TAG_NAME, 'li')
for link in linksLI:
    linksA.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))

## 2 deep
# click on the links
for link in linksA:
    ### start
    driver.get(link)
    ### body
    ## pg 2
    links2link = []
    links2 = driver.find_elements(By.TAG_NAME, 'a')
    for link in links2:
        try:
            if not link in links2link:
                links2link.append(link.get_attribute('href'))
            else:
                pass
        except Exception:
            pass
    
## 3 deep
for link in links2link:
    if 'microsoft' in link:
        ### start
        driver.get(link)
        ### body
        ## pg 2
        links3link = []
        try:
            links3 = driver.find_elements(By.TAG_NAME, 'a')
        except Exception:
            pass
        for link in links3:
            try:
                if not link in links3link:
                    links3link.append(link.get_attribute('href'))
                else:
                    pass
            except Exception:
                pass
    else:
        pass
### stop
driver.quit()
### after
## store data
linkdict = {
    '1':linksA,
    '2':links2,
    '3':links3
}
linkdictjson = json.dumps(linkdict, indent=4)
with open('Backups\MANUAL-FAILSAFE\WebScrapers\windowsERRORscraper\localdata.json', 'w') as loc:
    loc.write(linkdictjson)
