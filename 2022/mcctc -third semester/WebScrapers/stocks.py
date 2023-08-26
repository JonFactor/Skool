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
############## running #################

try:
    driver.get('https://finviz.com/insidertrading.ashx')
    time.sleep(1111)
finally:
    driver.quit()

    
################# Store in txt ##########################