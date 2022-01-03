
if '__name__' == '__main__':
    import pyautogui as pg
    print("how")



def mone(ruppee):


    f = open('''D://My projects//Vs code//Python//Projects//Account Balance('RIT bank')//account_ballance.txt''')
    content = f.read()

    f.close()
    inputs = ruppee


    moneys = int(content)+inputs

    fg = open('''D://My projects//Vs code//Python//Projects//Account Balance('RIT bank')//account_ballance.txt''', 'w')

    fg.write(f"{moneys}")

    fg.close()
