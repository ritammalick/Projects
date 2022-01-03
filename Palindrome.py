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
