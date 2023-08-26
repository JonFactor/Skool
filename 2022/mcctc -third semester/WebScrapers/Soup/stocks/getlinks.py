from bs4 import BeautifulSoup
from lxml import etree
import requests

page = requests.get('https://finviz.com/insidertrading.ashx')

pgcontent = BeautifulSoup(page.content, 'html.parser')

table = pgcontent.find(class_='body-table w-full bg-[#d3d3d3]')

for tr in table:
    pass
print(table)