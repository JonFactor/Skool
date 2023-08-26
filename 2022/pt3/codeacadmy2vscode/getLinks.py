### imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time, json
### functions
## basic functions
def getjson():
    global link, clientEmail, clientPass
    with open('Backups\MANUAL-FAILSAFE\codeacadmy2vscode\local.json', 'r') as loc:
        data = json.load(loc)
        link = data['link']
        clientEmail = data['email']
        clientPass = data['pass']
    link = 'https://www.codecademy.com/login?redirect=https%3A%2F%2Fwww.codecademy.com%2F'
def start():
    global driver

    #PATH = "C:\Program Files (x86)\chromedriver.exe"# Home
    PATH = 'C:\\Users\Factor_Jon\Desktop\chromedriver.exe' #Skool
    driver = webdriver.Chrome(PATH)
    getjson()
    driver.get(link)

   
def login():

    webwait(path='/html/body/div[2]/div/div/div[3]/main/div/div/div/div[2]/div/ul/li[2]/form/button')
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/main/div/div/div/div[2]/div/ul/li[2]/form/button').click()#googleBtn
    webwait(path='//*[@id="identifierId"]')
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(clientEmail, Keys.ENTER)#email
    webwait(path='//*[@id="password"]/div[1]/div/div[1]/input')
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(clientPass, Keys.ENTER)#pswrd

    
def cources():
    global Cils
    webwait(path='/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul/div/button')
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul/div/button').click()#viewAll
    webwait(path='/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul/li[1]/div[1]/button')
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul/li[1]/div[1]/button').click()#close
    Cul = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[1]/main/div/div[1]/div[1]/div/ul')#cil container
    Cils = Cul.find_elements(By.TAG_NAME, 'li')# cils
    
    courcesLoop()
    print('WeDone?')
def courcesLoop():
    global links
    links = []

    for c in Cils:
        cc = c.find_element(By.TAG_NAME, 'div')
        time.sleep(1)
        l = cc.find_element(By.TAG_NAME, 'button')
        l.click()
        time.sleep(1)
        silly = c.find_element(By.TAG_NAME, 'a')
        links.append(silly.get_attribute('href'))


def appendingListBox():
    global l1sdivs, k
    time.sleep(3)
    l = True
    k = 1
    while l:
        try:
            l1sbox = driver.find_element(By.XPATH, f'/html/body/div[{k}]/div/div[3]/div/div/div/section')
            l = False
        except Exception:
            k += 1
    i = 1
    l1sdivs = []
    o = True
    while o:
        try:
            l1sdivs.append(l1sbox.find_element(By.XPATH, f'/html/body/div[{k}]/div/div[3]/div/div/div/section/div[{i}]'))
            i += 1
        except Exception:
            o = False
def after():
    global lin, assignlinks, links
    for lin in links:
        assignlinks = []
        if not 'career-change-guide' in lin:
            driver.get(lin)
        else:
            bol = False

        time.sleep(6)
        menu = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/header/div/div[1]/div[3]/button')#openPathMenu
        menu.click()
        time.sleep(3)
        ## opening paths

        appendingListBox()

        i = 0
        l2sdivs = []
        while i < len(l1sdivs):
            div = l1sdivs[i]
            div.click()
            l2box = driver.find_element(By.XPATH, f'/html/body/div[{k}]/div/div[3]/div/div/div/section/div[{i+1}]/div')
            ii = 0
            o = True
            while o:
                try:
                    l2sdivs.append(l2box.find_element(By.XPATH, f'/html/body/div[{k}]/div/div[3]/div/div/div/section/div[{i+1}]/div/div[{ii+1}]'))
                    ii += 1
                    
                except Exception:
                    o = False
            i += 1
        ii = 0
        while ii < len(l2sdivs):
            div2 = l2sdivs[ii]
            time.sleep(1)
            try:
                div2.click()
                d = driver.find_element(By.XPATH, f'/html/body/div[{k}]/div/div[3]/div/div/div/section')
                f = d.find_elements(By.TAG_NAME, 'a')
                for l in f:
                    if not l.get_attribute('href') in assignlinks:
                        assignlinks.append(l.get_attribute('href'))

            except Exception:
                break
                pass
            ii += 1
        

        time.sleep(5)
        print(3)
        sendlinks()
        print(4)

def end():
    driver.close()
def sendlinks():
    deff = {
        'assginment':lin,
        'links':assignlinks
    }
    with open('Backups\MANUAL-FAILSAFE\codeacadmy2vscode\links.json', 'w') as li:
        json.dump(deff,li)
        li.close()
## class functions
def webwait(path, c = False, t = False):
    if t:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, path)))
    if not c:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, path)))
    else:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, path)))
    
### order
try:
    start()
    login()
    cources()
    after()
finally:
    end()