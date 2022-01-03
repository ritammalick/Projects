# quiz game
import time
import random
time.sleep(1)
print("****Welcome to the Quiz game****")
print()
time.sleep(.5)
print("So are you ready?\n Let's Begin")

time.sleep(1)
print("Choose a type\n Type 1 for Science\n 2 for computer\n 3 for riddle \n 4 for mixed ")
type = input("")
if type =='2':
    n = 3
    for i in range(3):

        print(n-i)
    print("1. Who is the inventor of computer?\na) Charles Babbage\n b) Thomas Alva Edison")