import pandas as pd
import numpy as np

import os
### imports ###
with open('BigBoyProj\Stocks\localdata.json', 'r') as op:
    stockdata = op.readlines()
    op.close()
print(stockdata)
### grab data ###

### use data ###
os.remove('BigBoyProj\Stocks\localdata.json')
### delete temp file ###