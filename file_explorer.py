import cv2
from tkinter import *
from tkinter import filedialog
root = Tk()
root.geometry('1200x1000')

def choose():
    file = filedialog.askopenfilename(initialdir='D:\\My projects', title='Choose', filetypes=(('png files','.png')))

choose_file = Button(
    text='Choose a file', command=choose
)
choose_file.pack()
root.mainloop()
