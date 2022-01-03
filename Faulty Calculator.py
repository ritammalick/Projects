a = input("Enter what you want to do: ")
num_1 = int(input("Enter First: "))
num_2 = int(input("Enter SEcond:"))


def n_calculator(): 

    
    if a == '+':
        add = num_1+num_2
        print(add)
    elif a=='-':
        sub = num_1-num_2
        print(sub)
        
if num_1==40 and num_2==50 and a=='+':
    print("1000")
else:
    n_calculator()


