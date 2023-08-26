import os, json

tickers = []
contents = []
for filename in os.listdir('WebScrapers\Selnium\StockScraper\data'):
    f = os.path.join('WebScrapers\Selnium\StockScraper\data', filename)
    with open(f, 'r') as reading:
        fJson = json.load(reading)
    tickers.append(filename.strip('.json'))
    if fJson == []: contents.append('null')
    else: contents.append(fJson)
print(len(tickers))
with open('WebScrapers\Selnium\StockScraper\ciks.json','r') as read:
    test = json.load(read)
print(len(test))