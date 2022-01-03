import random;l1 = [];l2 = [];l3 = []
def multiplication_bad(number):
    global n ; n = number
    for i in range(1,11):
        if i == 9:e = number*10;rand = random.randint(30,e);r = rand
        else:r = i * number
        l1.append(r)
def multiplication_good(num):
    for i in range(1,11):r = i * num ; l2.append(r)
multiplication_bad(9)
multiplication_good(n)
def detector():
    for i in range(10):
        if l1[i] == l2[i]: m = l2[i]
        else:d = f'"{l1[i]}"' ;  m = d
        l3.append(m)
detector()
print(l3, " This is the fraud");print(l2, " This is the real one")