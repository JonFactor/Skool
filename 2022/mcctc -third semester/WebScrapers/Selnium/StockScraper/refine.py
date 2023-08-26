import os, json

with open('WebScrapers\Selnium\StockScraper\\nasdaq_screener_1675399262900.csv','r') as file:
    data = []
    for line in file:
        data.append(line[:10].split(',')[0])
print(data)
with open('WebScrapers\Selnium\StockScraper\\refined.json','w') as flies:
    json.dump(data, flies)