import time

lines = int(input("Enter the number of lines\n"))
li = lines+1
li = int(li)
b = lines-1

t_f = int(input("Enter 1 or 0\n"))

if t_f == 0:
    boolean = True
elif t_f == 1:
    boolean = False

if boolean:
    for i in range(li):
        print('*' * i)
        time.sleep(.04)
        
else:
    for b in range(lines):
        print('*'*(lines-b))


'''
























                                         ***LOADING FINISHED***'''



