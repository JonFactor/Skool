############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
############### Defining ###############

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

############## running #################
driver.get('https://techwithtim.net')

search = driver.find_element(By.NAME,'s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

try:
    main = driver.find_element(By.ID, 'main')
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )

    articales = main.find_elements(By.TAG_NAME, 'article')
    for article in articales:
        header = article.find_element(By.CLASS_NAME, 'entry-summary')
finally:
    driver.quit()







############ after running #############