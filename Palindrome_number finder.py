a = input("Enter your number or text: ")
l1 = []
b = []
for i in range(len(a)):
    l1.append(a[i])
    
    b.append(a[i])

l1.reverse()
print(l1)
print(b)
if l1 == b:
    print("This is palindrome")
else:
    print("This is not palindrome")

