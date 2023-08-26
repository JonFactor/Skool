# Python Syntax: Medical Insurance Project
### defining
age = 28
sex = 0
bmi = 26.2
numOfChildren = 3
smoker = 0
insuranceCost = 250 * age - 128 * sex + 370 * bmi + 425 * numOfChildren + 24000 * smoker - 12500
## editing
change = 1
#age
#age += change
#BMI
#bmi += change
#SEX
sex += change
## equation 
NewinsuranceCost = 250 * age - 128 * sex + 370 * bmi + 425 * numOfChildren + 24000 * smoker - 12500
### diffrence 
if NewinsuranceCost > insuranceCost:
  diffrenceOfInsurance = NewinsuranceCost - insuranceCost
else:
  diffrenceOfInsurance = insuranceCost - NewinsuranceCost
### output
print(f'''
This persons insurance cost is {insuranceCost} dollars.
New insurance cost is {NewinsuranceCost}
The diffrence is {diffrenceOfInsurance}
The changed varible is bmi by {change}
''')