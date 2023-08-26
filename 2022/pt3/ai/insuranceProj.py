import os, path
from pathlib import Path
data = []
datalist = []
with open('C:\\Users\Factor_Jon\Documents\GitHub\Portfolioplz\Backups\MANUAL-FAILSAFE\\ai\insurance.csv', 'r') as insure:
    x = 0
    for line in insure:
        data.append(line)
    while x < len(data):
        if x / 6:
            datalist.append(data[x])
        x += 1


y = 0 
refineddata = []
while y < len(datalist):
    refineddata.append(str(datalist[y]).split(','))
    y += 1

persondata = []
datadict = {}
alldata= []
w = 0
for person in refineddata:
    for varible in person:
        if varible == person[0]:
            ages=(varible)
        elif varible == person[1]:
            genders=(varible)
        elif varible == person[6]:
            prices=(varible)
    persondata = [w, ages, genders, prices]

    alldata.append(persondata)
    w += 1
w = 0
def trends():
    global pricediffwithspot
    pricediffwithspot = 0
    for lis in alldata:
        if lis[0] > 1337 / 2:
           pricediffwithspot =- float(lis[3])
        else:
            pricediffwithspot =+ float(lis[3])
        pricediffwithspot = pricediffwithspot / len(alldata)
        if pricediffwithspot < 0:
            pricediffwithspot = 'the last 668 insurance prices are {} on avrage higher than the first 668'.format(pricediffwithspot*-1)
trends()
print(pricediffwithspot)