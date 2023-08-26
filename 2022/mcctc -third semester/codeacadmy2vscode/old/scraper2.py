############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time, json
############### Defining ###############

PATH = 'C:\\Users\Factor_Jon\Desktop\chromedriver.exe'
driver = webdriver.Chrome(PATH)
############## functions ###############
def webwait(path = '',by = 'X'):
    if by == 'X':
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'{path}')))
    if by == 'C':
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, f'{path}')))
    time.sleep(.5)
def login():
    ### grab info
    with open('Backups\MANUAL-FAILSAFE\codeacadmy2vscode\local.json', 'r') as loc:
        data = json.load(loc)
        link = data['link']
        clientEmail = data['email']
        clientPass = data['pass']
    
    try:
        ## click google
        google = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/main/div/div/div/div[2]/div/ul/li[2]/form/button')
        google.click()
        ## find
        
        email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
        email.send_keys(clientEmail, Keys.ENTER)

        pas = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        pas.send_keys(clientPass, Keys.ENTER)
    finally:
        pass
def everything():
    try:
        ## showall
        webwait(path = '/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul/div/button')
        showall = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul/div/button')
        showall.click()
    finally:
        pass
def nesting():

    webwait(path = '/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul/li[1]/div[1]/button')
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul/li[1]/div[1]/button').click()
    time.sleep(1)
    courcesdiv = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul')
    time.sleep(3)
    cources = courcesdiv.find_elements(By.TAG_NAME, 'li')
    for cource in cources:
        cource.click()
        time.sleep(1)
        stuffs = cource.find_elements(By.CLASS_NAME, 'container__YJuK08cLjX0jUBbGmQfHd dashboard__1GwpCIjA_oG0nwPre5P1wS showLine__1G83rE1KM7C0eEu8n0d3t_')
        for stuff in stuffs:
            link = stuff.find_element(By.CLASS_NAME, 'link__2iwRnyero2KOH7hPxRxxVN')
            print(link)
            link.click()

############## running ################# Lesson 
try:
    driver.get('https://www.codecademy.com/login?redirect=https%3A%2F%2Fwww.codecademy.com%2F')
    login()
    everything()
    nesting()

finally:
    time.sleep(100)
    driver.quit()
############ after running #############