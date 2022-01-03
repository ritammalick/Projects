# not works

import os
import pyautogui as pg
import time
import datetime as dt
import tkinter.messagebox as tsmg

def greet():
    pg.write("Happy BIrthday")
    

def opening_facebook():
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    time.sleep(9)
    pg.hotkey('win','up')
    pg.hotkey('ctrl', 'l')
    pg.write('facebook.com')
    pg.keyDown('enter')
    
# a = int(input("Enter: "))
# b=a*60
# time.sleep(b)
    
opening_facebook()
point = pg.position()

time.sleep(5)
pg.click(1227, 92)

time.sleep(4)
pg.click(1227, 270)

time.sleep(1)
greet()










# cursor = pg.moveTo(12, 50)



# Tim = dt.datetime.now()


# c=1





