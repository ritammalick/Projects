def palindrome(a):
    
    l1 = []
    b = []
    for i in range(len(a)):
        l1.append(a[i])
        
        b.append(a[i])

    l1.reverse()

    if l1 == b:
        return True
    else:
        return False




number = input("Enter the number: ")

def main():
    p_true = palindrome(number)
    if p_true == True:
        print(f"The next palindrome is {p_true}")
    elif p_true == False:
        p_false = 0
        c = number
        n = int(number)
        n = int(n)
        while p_false == 0:
            n+=1
            c = str(n)
            mii = palindrome(c)
            if mii == True:
                b = c
                p_false = 1
            
        
        print(b)
            
                

try:
    if int(number) < 10:
        print("Please Enter a greater number")
    else:
        main()
except Exception as e:
    print(e)