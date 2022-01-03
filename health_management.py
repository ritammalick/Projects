# Health Management
import datetime


# food
def log1(name):
    f = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\ritam-food.txt', 'a')
    f.write(name)
    f.close()
def log2(name2):
    f = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\bozo-food.txt', 'a')
    f.write(name2)
    f.close()
def log3(name3):
    f = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\bhakta-food.txt', 'a')
    f.write(name3)
    f.close()
# exercise
def log1ex(name):
    f = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\ritam-exercise.txt', 'a')
    f.write(name)
    f.close()
def log2ex(name2):
    f = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\bozo-exercise.txt', 'a')
    f.write(name2)
    f.close()
def log3ex(name3):
    f = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\bhakta-exercise.txt', 'a')
    f.write(name3)
    f.close()

# Main
try:
    # code for log
    mod = int(input("type 1 for log 2 for retrieve\n"))
    if mod ==1:
        person = int(input("Enter 1 for Ritam, 2 for Bozo, 3 for Bhakta : "))



        if person ==1:
            typ = int(input("Enter 1 for food , 2 for exercise"))
            if typ==1:
                food1 = input("Enter what you have ate: ")
                i = datetime.datetime.now()
                log1(f"[{i}] {food1}\n")
            elif typ==2:
                exercise = input("Enter what you have ate: ")
                i = datetime.datetime.now()
                log1ex(f"[{i}] {exercise}\n")
        elif person ==2:
            typ = int(input("Enter 1 for food , 2 for exercise"))
            if typ==1:
                food1 = input("Enter what you have done: ")
                i = datetime.datetime.now()
                log2(f"[{i}] {food1}\n")
            elif typ==2:
                exercise = input("Enter what you have done: ")
                i = datetime.datetime.now()
                log2ex(f"[{i}] {exercise}\n")
        elif person ==3:
            typ = int(input("Enter 1 for food , 2 for exercise"))
            if typ==1:
                food1 = input("Enter what you have ate: ")
                i = datetime.datetime.now()
                log3(f"[{i}] {food1}\n")
            elif typ==2:
                exercise = input("Enter what you have done: ")
                i = datetime.datetime.now()
                log3ex(f"[{i}] {exercise}\n")

        
        
# code for retrieve          
            
    elif mod ==2:
        person = int(input("Enter 1 for Ritam, 2 for Bozo, 3 for Bhakta : "))
        if person==1:
            typ = int(input("Enter 1 for food, 2 for exercise"))
            if typ ==1:
                o = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\ritam-food.txt')
                print(o.read())
                o.close()
            elif typ ==2:
                o = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\ritam-exercise.txt')
                print(o.read())
                o.close()
        elif person==2:
            typ = int(input("Enter 1 for food, 2 for exercise"))
            if typ ==1:
                o = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\bozo-food.txt')
                print(o.read())
                o.close()
            elif typ ==2:
                o = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\bozo-exercise.txt')
                print(o.read())
                o.close()
        elif person==3:
            typ = int(input("Enter 1 for food, 2 for exercise"))
            if typ ==1:
                o = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\bhakta-food.txt')
                print(o.read())
                o.close()
            elif typ ==2:
                o = open('D:\\My projects\\Vs code\\Python\\Projects\\Health Management\\bhakta-exercise.txt')
                print(o.read())
                o.close()
    
    

    
        
    
except ValueError as v:
    print("You have to type 0 or 1 not any other thing!")
