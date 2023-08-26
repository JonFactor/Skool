# Import libraries
from bs4 import BeautifulSoup
import requests
import csv
 
# Set the URL to scrape
url = "https://weather.com/weather/tenday/l/USCA0987:1:US"
i = 1
# Send a GET request to the URL and store the response
response = requests.get(url)
 
# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
 
contain = soup.find(class_ = "DailyForecast--DisclosureList--nosQS")

forecast_data = {}
forecast_data2 = []
for temp in contain:
  tem = temp.find(class_ = "DetailsSummary--highTempValue--3PjlX")
  tem = tem.text
  forecast_data2.append(tem)
  i += 1

forecast_data = forecast_data2



with open("forecast.csv", "w") as csv_file:
  # Create a CSV writer
  writer = csv.DictWriter(csv_file, fieldnames=["date", "description", "high", "low"])
 

 
  # Write the forecast data to the file
  writer.writerows(forecast_data) 
