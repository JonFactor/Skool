import yfinance as yf
import os
import json
import requests
from pathlib import Path
from datetime import datetime
import time
import urllib.request
### imports ###

if os.path.exists('BigBoyProj\Stocks\localdata.json'):
    with open('BigBoyProj\Stocks\localdata.json', 'r') as op:
        ticker = op.readline()
        op.close()
else:
    print('ABC')
    ticker = 'ABC'

### grab ticker ###
ticker = 'abc'
tick = yf.Ticker(ticker)
tickdata = tick.stats()
jsontick = json.dumps(tickdata)
### look up ticker ###### yFinance

### look up ticker ###### insider

with open('BigBoyProj\Stocks\localdata.json', 'w') as op:
    op.write(jsontick)
    op.close()
### send data to ai ###
responce = requests.get('https://api.sec-api.io/insider-trading')
result = responce.text
print(result)

import ai
### start ai.py ###