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

############### Defining ###############

#PATH = "C:\Program Files (x86)\chromedriver.exe"# Home
PATH = 'C:\\Users\Factor_Jon\Desktop\chromedriver.exe'
driver = webdriver.Chrome(PATH)
thelist = []
col = []
trnum = 0
rows = ''
num4rows = 100000
tdnum = 1
############## running #################

try:
    driver.get('https://finviz.com/insidertrading.ashx')
    time.sleep(1000)

    table_id = driver.find_element(By.XPATH, '/html/body/div[2]/div/table[2]')
    print('loaded')
    time.sleep(1)
    trnum +=2 
    while trnum <= num4rows:
        

        try:
            table_id.find_element(By.XPATH, f"/html/body/div[2]/div/table[2]/tbody/tr[{trnum}]/td[3]")
            print(trnum)
        except NoSuchElementException:
            trnum += 1
            pass
        
        

        
        rows = table_id.find_element(By.XPATH, f"/html/body/div[2]/div/table[2]/tbody/tr[{trnum}]")
        tdnum = 1
        while tdnum <= 10:
            try:
                rows.find_element(By.XPATH,f"/html/body/div[2]/div/table[2]/tbody/tr[{trnum}]/td[{tdnum}]")
            finally:
                col.append(rows.find_element(By.XPATH,f"/html/body/div[2]/div/table[2]/tbody/tr[{trnum}]/td[{tdnum}]").text) 
                tdnum += 1
        
        trnum+=1
finally:
    print('done')
    driver.quit()
    ############# Stopped ############
    Tag = []
    Name = []
    Position = []
    Date = []
    Type = []
    Cost = []
    Cps = []
    a = 0
    while a < len(col):
        Tag.append(col[a])
        a +=10
    a = 1
    while a < len(col):
        Name.append(col[a])
        a += 10
    a = 2
    while a < len(col):
        Position.append(col[a])
        a += 10
    a = 3
    while a < len(col):
        Date.append(col[a])
        a += 10
    a = 4
    while a < len(col):
        Type.append(col[a])
        a += 10
    a = 5
    while a < len(col):
        Cps.append(col[a])
        a += 10
    a = 8
    while a < len(col):
        Cost.append(col[a])
        a += 10
    ID = 0
    Tagsss = {}
    Positionss = {}
    Typess = {}
    Cpsss = {}
    Costss = {}
    Namess = {}
    Tagss = {}
    Datess = {}

    while ID < len(Tag):
        Tags = {ID: Tag[ID]}
        Names = {ID: Name[ID]}
        Positions = {ID: Position[ID]}
        Types = {ID: Type[ID]}
        Cpss = {ID: Cps[ID]}
        Costs = {ID: Cost[ID]}
        Dates = {ID: Date[ID]}
        Tagss.update(Tags)
        Namess.update(Names)
        Positionss.update(Positions)
        Typess.update(Types)
        Cpsss.update(Cpss)
        Costss.update(Costs)
        Datess.update(Dates)
        ID +=1

    AllData = [
        Tagss,
        "-------------END OF TAGS-------------------",
        Namess,
        "-------------END OF Names-------------------",
        Positionss,
        "-------------END OF Pos-------------------",
        Typess,
        "-------------END OF types-------------------",
        Cpsss,
        "-------------END OF CPS-------------------",
        Costss,
        "-------------END OF COST-------------------",
        Datess
    ]
    
################# Store in txt ##########################
DataDir = Path.cwd() / 'python' / 'WebScrapers' / 'TXTS'
if not os.path.exists(DataDir):
    DataDir.mkdir(parents=True, exist_ok=True)

ThisDataDir = DataDir / 'StockScraper'
if not os.path.exists(ThisDataDir):
    ThisDataDir.mkdir(parents=True, exist_ok=True)

Path(ThisDataDir / 'finviz').write_text(json.dumps(AllData))