from bs4 import BeautifulSoup
from requests import get


url = "https://mahoningctc.com/mcctc-high-school-staff"
response = get(url)

soup = BeautifulSoup(response.text, 'html.parser')

teachers = soup.find_all('tr')
print(teachers.text)