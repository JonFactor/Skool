############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path 
import re, json, os, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
############### Defining ###############

#PATH = "C:\Program Files (x86)\chromedriver.exe"# Home
PATH = 'C:\\Users\Factor_Jon\Desktop\chromedriver.exe'
driver = webdriver.Chrome(PATH)
thelist = []
col = []
trnum = 0
rows = ''
num4rows = 100
tdnum = 1

############## functions ###############
def clicky(x):
    WebDriverWait.until(EC.visibility_of_element_located((By.XPATH, x)))
    driver.find_element(By.XPATH, x).click()
def findy(x):
    WebDriverWait.until(EC.visibility_of_element_located((By.XPATH, x)))
    y = driver.find_element(By.XPATH, x)
    return y
def inputy(x, y):
    WebDriverWait.until(EC.visibility_of_element_located((By.XPATH, x)))
    driver.find_element(By.XPATH, x).send_keys(y, Keys.ENTER)
############## running #################
### make email
try:
    driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp') # start
    #inputy(x = )
except Exception:
    pass