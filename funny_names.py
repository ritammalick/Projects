# imports
import random

# lists
names = []
fun = []
first_name = []
last_name = []
funny_names = []

# inputs
num_friends = int(input("Enter the number of people\n"))
print("Enter the names")

# main
for i in range(num_friends):
    a = input("")
    names.append(a)

for c in range(num_friends):
    elements = names[c].split(" ")
    for i in range(2):
        fun.append(elements[i])   

for i in range(len(fun)):
    
    f = fun[i]
    if i%2 == 0:
        first_name.append(f)
    else:
        last_name.append(f)

for d in range(len(first_name)):
    rand = random.choice(last_name)
    last_name.remove(rand)
    r = f"{first_name[d]} {rand}"
    print(r)
