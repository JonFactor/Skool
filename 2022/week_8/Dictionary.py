#Dictionary: a book or electronic resource that lists the words of a language 
# (typically in alphabetical order) and gives their meaning, or gives the equivalent 
# words in a different language, often also providing information about pronunciation,
#  origin, and usage.

# In Programing - Key(Word or varible) : Value
# Key:Value Pairs

from multiprocessing.reduction import sendfds


sensors = {"livingroom":2, "diningroom":4, "kitchen":6, "basement":12, "bedroom":1}
print(sensors)
livingroom = sensors["livingroom"]
print(f"The Living Room has {livingroom}sensors in it ")
mrSekol = {"name": "Mr.S", "age": 27, "kids": True}
print(mrSekol)
print(mrSekol["name"])

pastries = {"donuts":["blueberry", "cream stick", "boston cream", "glazed"], "cake":["chocolate","vanilla", "lemon", "almond"], "cookies":["chocolate chip", "oatmeal", "lemon", "peanut butter"]}
print(pastries)
for item in pastries:
    print(item)

numOfMember = {}
numOfMember['silver'] = 27
numOfMember['gold'] = 21
numOfMember['platinum'] = 12
numOfMember['diamond']= 5
print(numOfMember)
numOfMember.update({'silver':44})
print(numOfMember)
numOfMember.update({"double diamond": 2})
print(numOfMember)

drinks = ['espresso', 'chai', 'decaf', 'americano']
caffine = [64, 40, 0, 120]
zippedCoffee = zip(drinks, caffine)
print(zippedCoffee)

