import requests
import os
from pathlib import Path
from datetime import datetime
import json

passed = False
while passed == False:
    query = input('Enter the book youd like to search: ')

    responce = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}")

    if responce.status_code == '404':
        print('Book Does not exist')
    else:
        passed = True

results = responce.json()
print(responce.json())
results = results['items']
results = results[4]
### make files ###
time = str(datetime.now().strftime("%H:%M:%S"))
time = time.replace(':','_')
resultsDir = Path.cwd() / 'python'/'schoolWork'/'apis'/'books' / f'result_{time}'
resultsDir.mkdir(parents=True, exist_ok=True)

Path(resultsDir / "RESULTS.txt").write_text(str(results))

