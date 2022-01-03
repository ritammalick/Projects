import random
from tkinter import *
import tkinter.messagebox as tsmg
score = 0

def rock():
    global score
    comp = random.randint(1, 3)
    global user
    user = 'r'
    
    if comp==2:
        print('you lose')
    elif comp ==3:
        print("youwin")
    else: print("Tied")
    score = score+10

def paper():
    comp = random.randint(1, 3)
    global user
    user = 'r'
    
    if comp==3:
        print('you lose')
    elif comp ==1:
        print("youwin")
    else: print("Tied")
    

def scissor():
    comp = random.randint(1, 3)
    global user
    user = 'r'
    
    if comp==1:
        print('you lose')
    elif comp ==2:
        print("you win")
        
    else: print("Tied")


tk = Tk()

butt1 = Button(text = 'Rock', command=rock)
butt1.pack()
butt2 = Button(text = 'Paper', command=paper)
butt2.pack()
butt3 = Button(text = 'Scissor', command=scissor)
butt3.pack()

labe = Label(text = "Rock")

if score ==10:
    labe.pack()



tk.mainloop()