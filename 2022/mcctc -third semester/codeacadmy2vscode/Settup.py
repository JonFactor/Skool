### imports
import tkinter as tk
from tkinter import  ttk, Label,Entry,Button
import wave, json, os
### defining
ww = 500
wh = 700
backround ='#f2f3ba'
Path = ''
jsonDir = 'Backups\MANUAL-FAILSAFE\codeacadmy2vscode\local.json'
### functions
def submit():
    if os.path.exists(jsonDir):
        os.remove(jsonDir)
    with open(jsonDir, 'w') as loc:
        json.dump(
            {
            'link':entLink.get(),
            'email':entEmail.get(),
            'pass':entPass.get()
            },loc)
        if  entLink.get() == '':
            print('oops')
        else:
            menu.destroy()
### ui
try:
    menu = tk.Tk() # start
    menu.geometry(f"{ww}x{wh}")
    menu.configure(bg = backround)
    menu.title('CodeCadamy2VS')
    # defining
    lbltitle = Label()
    lblLink = Label()
    entLink = Entry()
    lblEmail = Label()
    entEmail = Entry()
    lblPass  = Label()
    entPass = Entry()

    btnSubmit = Button()
    #configs
    lbltitle.configure(text='Code2VS',font=('Arial', 32), bg = backround)
    lblLink.configure(text='Link:',font=('Arial', 16), bg = backround)
    entLink.configure(font=('Arial', 16), bg = backround)
    lblEmail.configure(text='Email:',font=('Arial', 16), bg = backround)
    entEmail.configure(font=('Arial', 16), bg = backround)
    lblPass.configure(text='Password:',font=('Arial', 16), bg = backround)
    entPass.configure(font=('Arial', 16), bg = backround)

    btnSubmit.configure(text='Submit',font=('Arial', 30),command=submit)
    #packing
    lbltitle.pack()
    lblLink.pack()
    entLink.pack()
    lblEmail.pack()
    entEmail.pack()
    lblPass.pack()
    entPass.pack()

    btnSubmit.pack()
finally:
    menu.mainloop() # end



import scraper