from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
numba = 3
fors = "aaaaa"

for a in fors:
    web = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # opens google.
    web.get('https://explore.org/fat-bear-week')
    time.sleep(500)

    email = f'Jon.factor{numba}@gmail.com'

    vote = web.find_element(By.CLASS_NAME, 'poll-choice-vote btn btn-secondary btn-block')
    vote.click
    
    Email = web.find_element(By.ID, 'email_id')
    Email.send_keys(email)

    Robot = web.find_element(By.CLASS_NAME, 'recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-expired')
    Robot.click

    Sub = web.find_element(By.CLASS_NAME, 'btn form-button builder-button-style')
    Sub.click
    numba += 1