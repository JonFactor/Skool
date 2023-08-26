### imports
import tkinter as tk
from tkinter import  ttk, Label,Entry,Button
### defining
ww = 500
wh = 700
backround ='#f2f3ba'

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