import tkinter as tk
from tkinter.ttk import Label, Entry, Button
from ctypes import windll
##### imports ######
#### defs ####
soupp = True
def soup():
    global soupp
    soupp = True
def Stelnium():
    global soupp
    soupp = False
try:
    #### Starting #####
    window = tk.Tk()
    #### fix blurr ####
    windll.shcore.SetProcessDpiAwareness(1)
    #### title ####
    window.title('WebScraper')
    #### size ####
    window.geometry('700x500+50+50')
    #### Body #####
    Title = Label(window, text='AUTOMATION!!!', font=("Helvetica", 32))

    lblWebsiteURL = Label(window,font=("Helvetica", 18),text='URL:')
    entwebsiteURL = Entry(window, font=("Helvetica", 18))
    lblelementtype = Label(window,font=("Helvetica", 18),text='element type:')
    btnSoup = Button(window, text='Soup',command=soup)
    btnStelenium = Button(window, text='Stelenium',command=Stelnium)
    #btnSelnium = 

    Title.pack()
    btnSoup.pack(padx=1,side=tk.LEFT)
    btnStelenium.pack(padx=5,side=tk.LEFT)
    lblWebsiteURL.pack()    
    entwebsiteURL.pack()
    lblelementtype.pack()
    
    
    

finally:
    window.mainloop()

    #### after ####