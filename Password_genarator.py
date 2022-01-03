import random

rand = random.randint(1,10)

name = input("Enter your name: ")
birtdate = input("Enter your birtdate: ")
month = input("Enter your birth month: ")
lucky_num = input("Enter your lucky number: ")

def password_genarator():
    if rand == 1:
        password = name+birtdate+month+lucky_num
    elif rand == 2:
        password = birtdate+name+month+lucky_num
    elif rand ==3:
        password = name+birtdate+lucky_num+month
    elif rand ==4:
        password = birtdate+name+lucky_num+month
    elif rand ==5:
        password = name+month+birtdate+lucky_num
    else:
        password = lucky_num+name+birtdate+month

    return password

print(password_genarator())

