
from contextlib import nullcontext
from turtle import numinput
import requests
from bs4 import BeautifulSoup
import re
from itertools import islice

URL = "https://weather.com/weather/tenday/l/7ccb1832fa2a87ec02ce4b93334317724ad9be354b2f63026744350e81f5481c"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="WxuDailyCard-main-a43097e1-49d7-4df7-9d1a-334b29628263")
DailyInfo = results.find_all( class_="DaypartDetails--DetailSummaryContent--3uxcj Disclosure--SummaryDefault--3xAWB")



for Daily in DailyInfo:
    Day = Daily.find( class_="DetailsSummary--daypartName--2FBp2")
    High = Daily.find( class_="DetailsSummary--highTempValue--3Oteu")
    Low = Daily.find( class_="DetailsSummary--lowTempValue--3H-7I")
    Cloud = Daily.find( class_="DetailsSummary--extendedData--365A_")
    
    High = High.text
    Day = Day.text
    Low = Low.text
    Cloud = Cloud.text
    
    High = High.split("°")
    High = int(High[0])
    Low = Low.split("°")
    Low = int(Low[0])
    Day = Day.split(" ")
    Day = Day[0]
    
    Avrage = (High + Low) / 2



    if Cloud == "AM Showers" or "PM Showers":
        if Avrage <= 32:
            Snow = "There is a chance of snow in the area"
        else:
            Snow = "There is no chance of snow in the area"
    else:
        Snow = "There is no chance of snow in the area"

   
print(f"The day:{Day},  Avrage Temp:{Avrage},  Cloud conditions:{Cloud}, {Snow}")
    
SekolJon = input("Is this too sekol(S) or jon?(J):")
if SekolJon == 'J':
    receiver_email = "jon.factor2@gmail.com"
elif SekolJon == 'S':
    receiver_email = "Michael Sekol <michael.sekol@mahoningctc.com>"
else:
    print("ERROR: PLEASE TYPE EITHER AN S OR J")




#### Message Sender ####

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "Factor_Jon@student.mahoningctc.com"
password = input("Type your password and press enter: ")
message = f"""\
Subject: Weather

"The day:{Day},  Avrage Temp:{Avrage},  Cloud conditions:{Cloud}, {Snow}"""

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 

print("sent")



