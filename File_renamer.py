oldname = str(input("Enter the folder path of the file you want to rename\n"))
names = str(input("Enter the name of the file\n"))
import os
newname = str(input("Enter the new name\n"))

with open(f'{oldname}{names}') as name:
    
    old = name.read()
b = f'{oldname}{names}'
os.remove(b)
with open(f'{oldname}{newname}', 'w') as p:
    p.write(f'{old}')
