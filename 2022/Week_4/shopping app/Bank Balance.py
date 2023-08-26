from cmath import nan
payCheck = nan
userName = input(("Welcome, what is your name?"))
balance = 5000.25
deposits = float(input(("How muchof your paycheck would you ike to deposit")))
expenceItem = (input("what did you buy?"))
expenceAmount = float(input(f"how much does a {expenceItem} cost?"))

#customerName = input(("Welcome, what is your name?"))
startingBalance = 5000.25
#payCheck = float(input(("How muchof your paycheck would you ike to deposit")))
#expenditureItem = (input("what did you buy?"))
#expenditure = (input(f"how much does a {expenditureItem} cost?"))


print(f"Hello {userName} your starting balance is {startingBalance}")

def checkingBalance (userName, balance, deposits, expenceItem, expenceAmount):
    endingBalance = balance + deposits - expenceAmount
    customer_name = userName
    startingBalance = balance
    payCheck = deposits
    expenditure_items = expenceItem
    expenditure = expenceAmount
    print(f"Good Day, {customer_name}. After spending money on a {expenditure_items} in the amount of {expenditure}, your current checking balance is: {endingBalance} ")

checkingBalance(userName, balance, deposits, expenceItem, expenceAmount)