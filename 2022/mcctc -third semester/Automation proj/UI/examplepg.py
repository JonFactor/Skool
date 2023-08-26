import tkinter as tk
from ctypes import windll
##### imports ######
try:
    #### Starting #####
    window = tk.Tk()
    #### fix blurr ####
    windll.shcore.SetProcessDpiAwareness(1)
    #### title ####
    window.title('')
    #### size ####
    window.geometry('wxh+50+50')
    #### Body #####
    

finally:
    window.mainloop()

    #### after ####