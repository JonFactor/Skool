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
driver.get("https://tempail.com/")
email = finds('//*[@id="eposta_adres"]').get_attribute('data-clipboard-text')
time.sleep(1111)
driver.quit()
