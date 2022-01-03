import random
userguess = True
Rand = random.randint(1, 50)
score = 0

try:
    while userguess:
        userguess = input("Enter your number: ")
        score = score+1
        if int(userguess)>Rand:
            print("Enter a smaller number")
            print()


        elif int(userguess)<Rand:
            print("Enter a larger number")
            print()
        elif int(userguess)==Rand:
            print("You guessed it right")
            print()
            print(f"You guessed in {score} guesses")
            userguess = False
        if score == 10:
            
            print("You losed\n the game is over")
            break
    

except ValueError as v:
    print("Enter only Number")
        