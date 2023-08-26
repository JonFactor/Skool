############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path 
import re, json, os, time, random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random import Random
############### Defining ###############

#PATH = "C:\Program Files (x86)\chromedriver.exe"# Home
PATH = 'C:\\Users\Factor_Jon\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(PATH)
thelist = []
col = []
trnum = 0
rows = ''
num4rows = 100
tdnum = 1

############## functions ###############
def clicky(x):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, x)))
    driver.find_element(By.XPATH, x).click()
def findy(x):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, x)))
    y = driver.find_element(By.XPATH, x)
    return y
def inputy(x, y):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, x)))
    driver.find_element(By.XPATH, x).send_keys(y)
############## running #################
### make email

## get name
fname = []
lname = []
userlist = []
passlist = []
with open('yt\\names.txt', 'r') as name:
    for line in name:
        line = line.split(' ')
        fname.append(line[0])
        lname.append(line[1])
## get username
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
lenletters = int(len(letters)) - 1
x = 0
for letter in letters:
    if x < random.randint(6,30):
        userlist.append(letters[random.randrange(lenletters)])
    x+=1
user = ''
for char in userlist:
    user += char
## get password 
password = ''
x = 0
for letter in letters:
    if x < random.randint(6,30):
        passlist.append(letters[random.randrange(lenletters)])
    x += 1
for char in passlist:
    password += char
## get phonenumber
try:
    ## verify phone
    driver.get('https://receive-smss.com/')
    # get numbers
    container = findy('//*[@id="content"]/div[2]/div/div[1]/div')
    links = container.find_elements(By.TAG_NAME, 'a')
    phones = []
    for link in links:
        href = link.get_attribute('href')
        phones.append(href)
finally:
    pass
## fill out fourm
try:
    while True:
        ## start
        driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp') # start
        ## fill fourm
        inputy(x = '//*[@id="firstName"]', y = fname[random.randrange(1111)]) # first
        inputy(x = '//*[@id="lastName"]', y = fname[random.randrange(1111)]) # last
        inputy(x = '//*[@id="username"]', y = user) # user
        inputy(x = '//*[@id="passwd"]/div[1]/div/div[1]/input', y = password) # pass
        inputy(x = '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input', y = password) # pass
        clicky(x = '//*[@id="accountDetailsNext"]/div/button') # next
        time.sleep(.5)
        ## check if worked
        if driver.current_url != 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp':
            break
        else:
            pass
    ## input phone number
    phonenumints = ''
    while True:
        phonenum = phones[random.randrange(len(phones))]
        for char in phonenum:
            try: 
                int(char)
                phonenumints += char
            except Exception:
                pass
        inputy(x = '//*[@id="phoneNumberId"]', y = phonenumints)
        clicky(x = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        if driver.current_url != 'https://accounts.google.com/signup/v2/webgradsidvphone?flowName=GlifWebSignIn&flowEntry=SignUp&TL=ALbfvL2TfaSYj4-VL6JIFGNwZ-SVF7H6SM9CibUswjT6qvO1MIluGHFcYRMppOE6':
            break
        else:
            pass
    ## store user and pass
    userdata = {
        'fname':fname,
        'lname':lname,
        'user':user,
        'pass':password,
        'number': phonenum
    }
    with open('yt\\accounts.json', 'w') as users:
        json.dump(userdata,users)
    
finally:
    driver.quit()