# import
import random

# Game specific variables
runs_comp = 0
wickets_comp = 0
runs_user = 0
wickets_user = 0
toss_won = False

# Functions
def instructions():
    print("***INSTRUCTIONS***\na) Choose a number between 1 to 6")

def game():
    pass

def decison():

    if runs_comp>runs_user:
        print("YOU LOSED THE GAME")
    elif runs_user>runs_comp:
        print("YOU WON THE GAME")


def bowling():
    global runs_comp
    global wickets_comp
    global comp_score
    for b in range(5):
        for i in range(6):

            comp = random.randint(1,6)
            
            user = int(input("Enter: "))

            if wickets_comp==10:
                break

            elif user == comp :
                wickets_comp = wickets_comp+1
                print("Out!        ",runs_comp,"-", wickets_comp ,"\n" )

                

            elif user<7:
                runs_comp = runs_comp+comp
                comp_score = f"{runs_comp}-{wickets_comp}"

                if comp == 4 or comp == 6:
                    print(f"Computer hits {comp}                 {comp_score}\n")
                else:
                    print(f"Computer makes {comp} runs                {comp_score}\n")
                
            
            else:
                print("Enter correct num")
            
            
        print("Over is done")



def batting():
       
    global runs_user
    global wickets_user
    global user_score
    for b in range(5):
        for i in range(6):

            comp = random.randint(1,6)
            
            user = int(input("Enter: "))

            if wickets_user==10:
                break

            elif user == comp :
                wickets_user = wickets_user+1
                print("Out!        ",runs_user,"-", wickets_user ,"\n" )

                

            elif user<7:
                runs_user = runs_user+user
                user_score = f"{runs_user}-{wickets_user}"
                print("                ", user_score)

                
            
            else:
                print("Enter correct num")
                
        print("Over is done")


# main

a = int(input("Enter 1 for head, 2 for tails"))
toss = random.randint(1,2)
if a == toss:
    print("You won the toss\n")
    toss_won = True
else:
    print("You losed the toss")
    toss_won = False

if toss_won:
    a = input("Enter 1 for bat, 2 for ball")
    if a == '1':
        batting()
        print(user_score)
        bowling()
        decison()
    elif a =='2':
        bowling()
        print(comp_score)

        print(f"\n Target - {runs_comp} in 30 balls\n")
        input("Press Enter Key to continue -- ")
        batting()
        decison()
else:
    print("Computer choosed batting")
    bowling()
    print(comp_score)
    batting()
    decison()




