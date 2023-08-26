
##### imports ######
import tkinter as tk
from ctypes import windll
from tkinter.ttk import Label, Entry, Button

### functions ###
def sub():
    identification=idVar.get()
    password = passVar.get()
    print(identification, password)
    idVar.set('')
    passVar.set('')
    import login
def see():
    pass 


try:
    #### Starting #####
    window = tk.Tk()
    #### fix blurr ####
    windll.shcore.SetProcessDpiAwareness(1)
    #### title ####
    window.title('SingUp')
    #### window size ####
    windowW = 600
    windowH = 900
    #### screen size ####
    screenW = window.winfo_screenmmwidth()
    screenH = window.winfo_screenheight()
    #### screen center #### 
    centerX = int(screenW / 2 - windowW / 2)
    centerY = int(screenH / 2 - windowH / 2)
    #### setting window size ####
    window.geometry(f'{windowW}x{windowH}+{centerX}+{centerY}')
    #### make resizable ####
    window.resizable(windowW,windowH)
    #### msc attributes ####
    #### transfarency ####
    window.attributes('-alpha',1)
    #### order ####
    window.attributes('-topmost',1)
    #up window.lift()
    #down window.lower()
    #### icon ####
    window.iconbitmap('python\Automation proj\images\Screenshot 2023-01-04 111710.ico')
    #### Body #####
    #title


    # ID
    idVar = tk.StringVar()
    idLBL = Label(window, text='ID ',font=('Helvetica', 12))
    idLBL.pack()
    idin = tk.Entry(window, textvariable= idVar,font=('calibre',10,'normal'))
    idin.pack()
    # Pass
    passVar = tk.StringVar()
    passLBL = Label(window, text='Password ',font=('Helvetica', 12))
    passLBL.pack()
    passin = tk.Entry(window, textvariable= passVar,font=('calibre',10,'normal'), show = '*')
    passin.pack()
    showBTN= Button(window,text='VIEW',command=see)
    showBTN.pack()
    # submit btn
    subBtn=tk.Button(window,text='SUBMIT', command=sub)
    subBtn.pack()


finally:
    window.mainloop()

#### after ####
