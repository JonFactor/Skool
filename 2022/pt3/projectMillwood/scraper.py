### SET TO TRUE IF YOU WANT MANUAL 
manual =False
import os
from pathlib import Path
from datetime import datetime as dt
from datetime import timedelta, date
import pathlib, json, pyodbc, time, re, datetime


### settings
## cheeky varibles
TowerDir = Path('C:/TOWER')
link = 'https://esp.chep.com/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html'
plantID = 'USG8'
bdate = date.today() - timedelta(days=8)
bweekday = bdate.weekday()
match bweekday:
    case 0: bdate -= timedelta(days=1)
    case 1: bdate -= timedelta(days=2)
    case 2: bdate -= timedelta(days=3)
    case 3: bdate -= timedelta(days=4)
    case 4: bdate -= timedelta(days=5)
    case 5: bdate -= timedelta(days=6)
byear = int(bdate.year)
bmonthnum = int(bdate.month)
bday = int(bdate.day)

ayear = 2022
amonthnum = 2
aday = datetime.time
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
### get username and password
conn = pyodbc.connect('DRIVER={SQL Server};'
                     'SERVER=PUTER\SQLEXPRESS;'
                     'DATABASE=onomatopoeia;'
                     'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute(f'SELECT * FROM mCompany')

for rowe in cursor:
    user = rowe[0]
    passs = rowe[1]
## make dir
if not os.path.exists(TowerDir):
    TowerDir.mkdir()
### make CSV
def writecsv():
    with open(f'{TowerDir}\\CSV.json', 'w') as twr:
        data = {
            'plantID': input('Whats the plan id:'),
            'bbyear' : input('Before Year:'),
            'bbmonthnum' : input('Before Month Number:'),
            'bbday' : input('Before Day Number:'),
            'bayear' : input('After Year:'),
            'bamonthnum' : input('After Month Number:'),
            'baday' : input('After Day Number:')
        }
        
        json.dump(data, twr)
        twr.close()
## opening CSV
def opencsv():
    global plantID, bmonthnum, bday, bmonthnum, byear, bmonthnum, ayear, amonthnum, aday
    with open(f'{TowerDir}\\CSV.json', 'r') as twr:
        csv = json.load(twr)
        twr.close()
    plantID = csv['plantID']
    byear = int(csv['bbyear'])
    bmonthnum = int(csv['bbmonthnum'])
    bday = int(csv['bbday'])
    ayear = int(csv['bayear'])
    amonthnum = int(csv['bamonthnum'])
    aday = int(csv['baday'])
if not manual:
    opencsv()
else:
    writecsv()
    opencsv()
### Webscraper
## imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, string, re, os, time
## varibles
PATH = "C:\Program Files (x86)\chromedriver.exe"# Home

driver = webdriver.Chrome(PATH)
## functions
def datesloop(number, path, path2, TF, mont, day):
    if not day:
        btn = driver.find_element(By.XPATH, path2) # '//*[@id="__jsview26--Data{TF}-cal--Head-B2"]'
        btn.click()
    container = driver.find_element(By.XPATH, path)
    rows = container.find_elements(By.TAG_NAME, 'div')

    if not mont:
        for row in rows:
            try:
                rowint = int(row.text)
                if rowint == number:
                    row.click()
                    break
                else:
                    pass
            except Exception:
                pass
    else:
        for row in rows:
            try:
                for month in months:
                    if month == row.text:
                        row.click()
                        break
                    else:
                        pass
            except Exception:
                pass

def dates( year, monthnum, day, TF):
    findsclick(f'//*[@id="__jsview26--Data{TF}"]/div')
    datesloop(year, f'//*[@id="__jsview26--Data{TF}-cal--YP"]', f'//*[@id="__jsview26--Data{TF}-cal--Head-B2"]', TF, False, False)
    datesloop(monthnum, f'//*[@id="__jsview26--Data{TF}-cal--MP"]', f'//*[@id="__jsview26--Data{TF}-cal--Head-B1"]', TF, True, False)
    datesloop(day, f'//*[@id="__jsview26--Data{TF}-cal--Month0-days"]', f'//*[@id="__jsview26--Data{TF}-cal--Month0-days"]', TF, False, True)
    
    dayscontainer = driver.find_element(By.XPATH, f'//*[@id="__jsview26--Data{TF}-cal--Month0-days"]')
    dayscontainerdivs = dayscontainer.find_elements(By.TAG_NAME, 'div')
    time.sleep(1)
    for div in dayscontainerdivs:
        try:
            divint = int(div.text)
            if divint == day:
                div.click()
                break
            else:
                pass
        except Exception:
            pass
    
def findsclick(x):
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).click()
    except Exception:
        pass
def findsEntry(x, y):
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, x)))
        c = driver.find_element(By.XPATH, x)
        c.send_keys(y)
        c.send_keys( Keys.ENTER)
    except Exception:
        pass
## staring up
driver.get(link)

## login

findsEntry('//*[@id="USERNAME_FIELD-inner"]', user)
findsEntry('//*[@id="PASSWORD_FIELD-inner"]',passs)
findsclick('//*[@id="LOGIN_LINK"]')
## us reports
driver.get('https://esp.chep.com/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html?sap-client=600&sap-language=EN#ZESP_USREPORTS-display')
## open reports

findsclick('//*[@id="__jsview26--onRepSelect"]')
findsclick('//*[@id="__item2-__jsview26--onRepSelect-3"]')

idspace = driver.find_element(By.XPATH, '//*[@id="__jsview26--mPlant-inner"]')
idspace.send_keys(Keys.CONTROL + 'a', Keys.DELETE)

findsclick('//*[@id="__jsview26--mPlant"]/div')
findsclick('//*[@id="__item3-plantName-0"]')
findsclick('//*[@id="accept"]')

dates( byear, bmonthnum, bday, 'From')### before
dates( ayear, amonthnum, aday, 'To')### after

findsclick('//*[@id="__button10"]')

while True:
    try:   
        findsclick('//*[@id="__jsview27--Export"]')
        break
    except Exception:
        pass
    
### end
driver.quit()