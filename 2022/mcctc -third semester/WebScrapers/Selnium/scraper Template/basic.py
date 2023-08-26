from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def finds(x , TAG = False, multiple = False, parent = None ,t = 5):
    try:
        if not TAG:
            WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.XPATH, x)))
            if parent == None:
                if not multiple: return driver.find_element(By.XPATH, x)
                else: return driver.find_elements(By.XPATH, x)
            else:
                if not multiple: return driver.find_element(By.XPATH, x)
                else: return parent.find_elements(By.XPATH, x)
        else:
            WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.TAG_NAME, x)))
            if parent == None:
                if not multiple: return driver.find_element(By.TAG_NAME, x)
                else: return driver.find_elements(By.TAG_NAME, x)
            else:
                if not multiple: return driver.find_element(By.TAG_NAME, x)
                else: return parent.find_elements(By.TAG_NAME, x)
    except Exception:
        return None