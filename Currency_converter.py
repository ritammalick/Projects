from tkinter import *
import tkinter.messagebox as tsmg


def getval():
    try:
        b = fromvar.get()
        c = tovar.get()
        if b=='rupee' and c=='dollar':

            answer = (float(from_entry.get())/74.89)
        
            tsmg.showinfo("Currency Converter", answer)
        
        elif b=='rupee' and c=='euro':
            answer = (int(from_entry.get())*86.57)
            tsmg.showinfo("Currency Converter", answer)

        elif b=='dollar' and c=='rupee':
            answer = (float(from_entry.get())*74.89)
            tsmg.showinfo("Currency Converter", answer)

        elif b=='dollar' and c=='euro':
            answer = (float(from_entry.get())/0.87)
            tsmg.showinfo("Currency Converter", answer)

        elif b=='euro' and c=='rupee':
            answer = (float(from_entry.get())/86.57)
            tsmg.showinfo("Currency Converter", answer)

        elif b=='euro' and c=='dollar':
            answer = (float(from_entry.get())*0.87)
            tsmg.showinfo("Currency Converter", answer)
        else :
            print()
    except Exception as e:
        print(e)
root = Tk()
root.title('Currency Converter')
root.geometry('450x470')
# root.minsize(375,240)
# root.maxsize(400,300)

# head = Label(text="Currency converter")
# head.grid(row=0,column=0)
heading= Label(root, text="Ritam's Currency converter", font = "lucida 18", relief=SUNKEN, bg='lightblue')
heading.grid(row=0, column=1)

blank = Label(root, text = '')
blank.grid(row=1, column=1)
fromvar = StringVar()
fromvar.set("From")
froms = OptionMenu( root, fromvar,'euro','dollar', 'rupee')

froms.grid(row=2, column = 0)

tovar = StringVar()
tovar.set("To")
to = OptionMenu( root, tovar,'euro','dollar', 'rupee')

to.grid(row=3, column = 0)

from_entry_var = IntVar
from_entry = Entry(root,textvariable=from_entry_var)
from_entry.grid(row=2, column=1)



butt1 = Button(text = 'Convert', command=getval)
butt1.grid(row=4,column=0)
root.mainloop()

