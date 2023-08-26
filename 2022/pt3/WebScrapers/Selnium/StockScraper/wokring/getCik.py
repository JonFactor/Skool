from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path 
import os 
import re 
import json, random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('C:\\Users\Factor_Jon\Desktop\chromedriver.exe')

driver.get('https://www.sec.gov/include/ticker.txt')
time.sleep(1)
x = driver.find_element(By.TAG_NAME, 'pre').text
y = x.split('\n')
ys = []
for stuff in y:
    ys.append(stuff.split(' '))

with open('D:\CodeShit\CIKS.json', 'w') as write:
    json.dump(ys, write)