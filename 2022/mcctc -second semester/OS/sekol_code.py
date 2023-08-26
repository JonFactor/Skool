import os
from time import sleep

def CLEAR_CONSOLE():
    #windows
    if os.name == "nt":
        return os.system('cls')

    # mac and linux
    else: 
        return os.system('clear')

