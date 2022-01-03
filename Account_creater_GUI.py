import time
from tkinter import *
import tkinter.messagebox as tsmg

    

def getvalue():
    names = name.get()
    bames = address.get()
    eames = email.get()
    paems = password.get()
    aaems = slide.get()

    with open('D:\\My projects\\Vs code\\Python\\Projects\\Account creator\\account_info_created_by account_creator', 'w') as info:
        info.write(f"Name - {names}\nAddress - {bames}\n Email - {eames}\n Password - {paems}\n Age - {aaems}")
    tsmg.showinfo("Account Creator", "Sucsessfully updated!")

tk = Tk()
tk.title("Account Creator - Untitled")

def exits():
    q = tsmg.askquestion("Account Creator", "Are you sure you want to exit?")
    
    if q=='yes':
        quit()
    else:
        pass



tk.geometry('380x320')

tk.minsize(375,240)
tk.maxsize(400,300)

heading= Label(tk, text="Ritam's Account Creator", font = "lucida 18", relief=SUNKEN, bg='lightblue')
heading.grid(row=0, column=0) 


namevalue = StringVar()
addressval = StringVar()
emailval = StringVar()
intval = StringVar()


frame = Frame(tk, borderwidth=0, padx=4, pady = 12)
frame.grid()
bb = Label(frame, text="Name: ", font='comicsanms 12',pady=2)
cc= Label(frame, text="Address: ", font='comicsanms 12')
dd = Label(frame, text="Email: ", font='comicsanms 12')
ee = Label(frame, text="Password: ", font='comicsanms 12')
ff = Label(frame, text="Age: ", font='comicsanms 12')
bb.grid(row=5, column=0)
cc.grid(row=6, column=0)
dd.grid(row=7, column=0)
ee.grid(row=8, column=0)
ff.grid(row=9, column=0)
name = Entry(frame, textvariable=namevalue, width=45)
address = Entry(frame, textvariable=addressval, width=45)
email = Entry(frame, textvariable=emailval, width=45)
password = Entry(frame, textvariable=intval, width=45)

name.grid(row=5, column=1)
address.grid(row=6, column=1)
email.grid(row=7, column = 1)
password.grid(row=8, column=1)
b = Button(text='Submit', command=getvalue, relief=RIDGE, fg="black", bg = "lightblue", width=12)
c = Button(text='Exit', command=exits, relief=RIDGE, fg="black", bg = "lightblue", width=12)
slide = Scale(orient='horizontal', length=300)
slide.grid(row=9, column=0, pady=10)

b.grid(row=10, column=0)
c.grid()



# text = Text(font='lucida', width=20)
# text.grid()

tk.mainloop()



