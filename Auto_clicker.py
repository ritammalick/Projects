import pyautogui
import time

many = int(input("Enter how many times you want to reepeat: "))
times = int(input("After how many seconds do you want to start: "))

time.sleep(times)

for i in range(many):
    pyautogui.tripleClick()
