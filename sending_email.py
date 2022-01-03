import pyautogui
import os
import time
from tkinter import *



person = input("Enter Email : ")
subject = input("Enter the subject : ")
main = input("Enter the main content : ")


pyautogui.hotkey('alt','tab')
pyautogui.write('gmail.com')
pyautogui.press('enter')
time.sleep(9)
pyautogui.click(62,169)
time.sleep(20)
pyautogui.write(person)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(subject)
pyautogui.press('tab')
pyautogui.write(main)
pyautogui.hotkey('ctrl', 'enter')