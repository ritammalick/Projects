base = '''
 1 | 2 | 3 
-----------
 4 | 5 | 6 
------------
 7 | 8 | 9 

'''
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
  a = str(input("enter 1 to 9"))
  
  if a in num: 
    num.remove(a)
    base.replace('1' ,'X')
    print(base)

print(base[2])

