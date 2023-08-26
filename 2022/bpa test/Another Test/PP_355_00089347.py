#00089347
import random
#setting varibles
DialCounter = 0
comboCounter= 0
b = 0
HowManyDials = 0
LockCombos = 0 
number = 0
numberList = []
def get_number_in_dials():
    #input for dials
    global HowManyDials
    HowManyDials = input("Each lock has how many dials? ")
    if int(HowManyDials) < 3:
        HowManyDials = 0
        get_number_in_dials()
    
    


def get_how_many_to_list():
    #input for combinations
    global LockCombos
    LockCombos = input("How many combinations should i generate? ")
    print("--------------")
    

def get_number():
    #random number generator
    global number,min, max,  numberList
    min = 0
    max = 9
    number = random.randrange(min, max)
    numberList.append( number)
    
    
def next_combo_number():
    #logic behind using all of the other statments
    global comboCounter,  DialCounter
    
    while int(LockCombos) > comboCounter:
        
        while DialCounter < int(HowManyDials):
            get_number()
            
            
            DialCounter = DialCounter + 1
        
        printState()
        DialCounter = 0
        comboCounter = comboCounter + 1
       
       
    


        
def printState():
    #prints and clears combos

    print(f"Number {comboCounter + 1}: {numberList}")
    numberList.clear()
    
#runs functios in order
get_number_in_dials()
get_how_many_to_list()
next_combo_number()
#prints the end of the program
print("--------------")
print(f"{comboCounter} random combinations were generated")