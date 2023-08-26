
from contextlib import nullcontext
from turtle import numinput
import requests
from bs4 import BeautifulSoup

URL = "https://forecast.weather.gov/MapClick.php?lat=41.0981&lon=-80.6508#.YzHIIXbMJD8"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="seven-day-forecast")
DailyInfo = results.find_all( class_="tombstone-container")

print(DailyInfo)
for Daily in DailyInfo:
    Day = Daily.find("p", class_="period-name")
    High = Daily.find("p", class_="temp temp-high")
    Low = Daily.find("p", class_="temp temp-low")
    print(High, Low)
    





#Location = input("where are you? ")
#System = input("Do you use the best system of measurements (y/n):")
#SysInput = numinput
#if System == y:
#    SysInput = "METRIC"
#elif System == n:
#    SysInput = "IMPERIAL"
#else:
#    SysInput = "METRIC"
#    print("Please type y or n, next time")



