from decimal import ROUND_DOWN
from turtle import numinput


pennies = int(input("How many pennies do you have :"))
dollar = 0
quarters = 0
dimes = 0
nickels = 0


if pennies >= 100:
    dollar = pennies / 100
    dollar = round(dollar)
    pennies -= dollar * 100


if pennies >= 25:
    quarters = pennies / 25
    quarters = round(quarters)
    pennies -= quarters * 25


if pennies >= 10:
    dimes = pennies / 10
    dimes = round(dimes)
    dimes -= dimes * 10


if pennies >= 5:
    nickels = pennies / 5
    nickels = round(nickels)
    nickels -= nickels * 5

coinList = [dollar, quarters, dimes, nickels, pennies]

print(f'''
Dollar Bills = {dollar}
Quarters = {quarters}
Dimes = {dimes}
Nickels = {nickels}
Pennies = {pennies}
''')