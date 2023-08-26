### imports
import os
import json
import tkinter as tk
from tkinter import  ttk, Label,Entry,Button
### definging
timeinday = 24
info = {}
info = json.dumps(info)
readinfo = {}
ww = 500
wh = 700
backround ='#f2f3ba'
### functions
## input
def menus():
    global menu
    try:
        menu = tk.Tk() # start
        menu.geometry(f"{ww}x{wh}")
        menu.configure(bg = backround)
        menu.iconbitmap('BigBoyProj\SCEDUAL\clock4.ico')
        menu.title('Scedual')
        # defining
        lbltitle = Label()
        btnLast = Button()
        btnNew = Button()
        btnList = Button()
        btnexit = Button()
        #configs
        lbltitle.configure(text='Scedual',font=('Arial', 32), bg = backround)
        btnLast.configure(text='LAST',font=('Arial', 16))
        btnNew.configure(text='NEW',font=('Arial', 16),command=new())
        btnList.configure(text='LOAD',font=('Arial', 16))
        btnexit.configure(text='EXIT',font=('Arial', 16))
        #packing
        lbltitle.pack()
        btnLast.pack(ipady=1, ipadx=50)
        btnNew.pack(ipady=1, ipadx=50)
        btnList.pack(ipady=1, ipadx=50)
        btnexit.pack(ipady=1, ipadx=50)
    finally:
        menu.mainloop() # end
def new():
    pass
## files
def save():
    if not os.path.exists('BigBoyProj\SCEDUAL\\inputs.json'):
        with open('BigBoyProj\SCEDUAL\\inputs.json', 'w') as store:
            store.write(info)

def read():
    with open('BigBoyProj\SCEDUAL\\inputs.json', 'r') as store:
        readinfo = store.read()
        return readinfo

def delete():
    os.remove('BigBoyProj\SCEDUAL\\inputs.json')

### order of functions

menus()