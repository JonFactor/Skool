### imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time, json, random
### functions
def start():
    global driver

    #PATH = "C:\Program Files (x86)\chromedriver.exe"# Home
    PATH = 'C:\\Users\Factor_Jon\Desktop\chromedriver.exe' #Skool
    driver = webdriver.Chrome(PATH)
    getjson()
def end():
    driver.quit()
def getjson():
    global links, clientEmail, clientPass
    with open('Backups\MANUAL-FAILSAFE\codeacadmy2vscode\links.json', 'r') as k:
        data = json.load(k)
        links = data['links']
    with open('Backups\MANUAL-FAILSAFE\codeacadmy2vscode\local.json', 'r') as loc:
        datas = json.load(loc)
        clientEmail = datas['email']
        clientPass = datas['pass']
def weirdlogin():
    
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div/div/div[2]/button')))
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div/div/div[2]/button').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/ul/li[2]/form/button').click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
        driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(clientEmail, Keys.ENTER)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(clientPass, Keys.ENTER)
    except Exception:
        pass
def login():
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[2]/div/div/div/div[1]/div[3]/ul/li[2]/form/button')))
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[2]/div/div/div/div[1]/div[3]/ul/li[2]/form/button').click()
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
        driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(clientEmail, Keys.ENTER)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(clientPass, Keys.ENTER)
    except Exception:
        pass
def holyshitwhocodedthisgayasswebsite():
    global titletxt, codetxt,typeetxt, textbox, h1
    titletxt = ''
    h1 = ''
    codetxt = ''
    typeetxt = ''
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div')))
        textbox = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div').text
        h1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div/h1').text.replace(' ', '-').replace('/', '-or-').replace('?', '')
    except Exception:
        pass
    try:
        code = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[4]')
        codetxt = code.text
        try:
            title = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div/div/div[1]/div/div/div/div[2]/div/span')
            titletxt = title.text.replace(' ', '-')
        except Exception:
            pass
        try:
            typee = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/button/div')
            typeetxt = typee.text.split('.')[1]
        except Exception:
            try:
                typee = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/button[2]/div')
                typeetxt = typee.text.split('.')[1]
            except Exception:
                pass
    except Exception:
        pass
def storecode():
    if titletxt != '':
        if typeetxt != '':
            with open(f'C:\\Users\jonfa\Documents\GitHub\Portfolio\Backups\MANUAL-FAILSAFE\codeacadmy2vscode\Work\\{titletxt.capitalize()}.{typeetxt}', 'w') as g:
                g.writelines(codetxt)
        else:
            with open(f'C:\\Users\jonfa\Documents\GitHub\Portfolio\Backups\MANUAL-FAILSAFE\codeacadmy2vscode\Work\\{titletxt.capitalize()}', 'w') as g:
                g.writelines(codetxt)
    elif h1 != '':
        with open(f'C:\\Users\jonfa\Documents\GitHub\Portfolio\Backups\MANUAL-FAILSAFE\codeacadmy2vscode\Work\\{h1}.txt', 'w') as g:
            g.writelines(textbox)         
### order
start()
for link in links:

    time.sleep(.5)
    driver.get(link)
    weirdlogin()
    login()
    holyshitwhocodedthisgayasswebsite()
    storecode()

end()