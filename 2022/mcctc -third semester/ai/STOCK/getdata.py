### imports
import yfinance as yf
import pandas as pd
import numpy as np
import csv
### code
## user
user = 'jonfa'
## ticker
strtick = 'AAPL'
try:
    tick = yf.Ticker(strtick)
except Exception:
    print("Ticker not found")
## get data
history = tick.history(period="max")

## store data
history.to_csv(f"C:\\Users\{user}\Desktop\Stocks\data\{strtick}.csv", index=False)