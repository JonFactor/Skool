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
### varibles
x = 0
### functions
def findsclick(x):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).click()
    except Exception:
        pass
def findsEntry(x, y):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, x)))
        driver.find_element(By.XPATH, x).send_keys(y)
    except Exception:
        pass
def finds(x):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, x)))
        return driver.find_element(By.XPATH, x)
    except Exception:
        return None
### start
driver = webdriver.Chrome()
driver.get("https://www.twitch.tv/")
## Sign Up Btn
findsclick('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button')
## Inputs
from usernames import newusers, passwords
username = newusers[x]
password = passwords[x]
findsEntry('//*[@id="signup-username"]', username)
findsEntry('//*[@id="password-input"]', password)
time.sleep(1)
findsclick('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/form/div[2]/button[2]')
## phone number
findsclick('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/form/div[1]/div/div[1]/div[2]/button')
## email instead of phone
import verify
from verify import email
findsEntry('//*[@id="email-input"]', email)
### end
driver.quit()