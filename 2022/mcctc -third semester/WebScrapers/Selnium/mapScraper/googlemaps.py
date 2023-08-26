############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
############### Defining ###############

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

############## running #################
driver.get('https://www.google.com/maps/@40.3662685,-81.2390813,7.96z')

search = driver.find_element(By.XPATH,'//*[@id="searchboxinput"]')
search.send_keys('Used Cars')
search.send_keys(Keys.RETURN)
time.sleep(5)

infobtn = driver.find_element(By.CLASS_NAME,'hfpxzc')
infobtn.click()
time.sleep(5)

website = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[13]/div[5]/a/div[1]/div[2]/div[1]')
time.sleep(50)

driver.quit()
