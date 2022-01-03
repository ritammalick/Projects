# Account creator

import time

print("HI WELCOME TO THE RITAM'S ACCOUNT CREATOR")
time.sleep(1.5)
print("I will question something from you")


name = input("What's your name\n")
address = input("What's your address\n")
email = input("What's your email\n")
password = input("Create a password for your account (It must be of atleast 5 characters)")
if len(password)<5:
    print("Confirm your password")
    passwor = False
    passwords = input("Enter your password again")
 
with open('D:\\My projects\\Vs code\\Python\\Projects\\Account creator\\account_info_created_by account_creator', 'w') as info:
    info.write(f"Name - {name}\nAddress - {address}\n Email - {email}\n password - {password}")    