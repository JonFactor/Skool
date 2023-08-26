from asyncio import sleep
import sekol_code as sc

sc.CLEAR_CONSOLE()
def theAnswer():
    password = input("What is the answer to life, the universe and everything ")

    if(password == '42'):
        print("Welcome wise one. I see you've traveled the Galaxy. Let's begin.")
        sleep(2)
        sc.CLEAR_CONSOLE()
    elif(password == "bob"):
        print("This is no time for jokes")
    elif(password == "tom"):
        print("Ah yes. The funny cat that chases that mouse")
    else:
        print("Isee you are new, Go get more experance and come back")

def level1():
    print("The man opens the door")
    sleep(2)
    print("An old wizard aproches you")
    sleep(2)
    beginQuest = input("Are you ready to begin your advantures? y/n")
    if(beginQuest == "y"):
        print("The adventure begins..")
    else:
        print("You're correct. Best if youget some sleep")

theAnswer()