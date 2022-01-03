import random

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
Guess_1 = 0
Guess_2 = 0
Lives_remianing = 10
player_1_choice = int(0)
player_2_choice = int(0)

rand_n = random.randint(a, b)
# print(rand_n)
print(f"Player 1: \n\n")

while player_1_choice!=rand_n:
    Guess_1 += 1
    Lives_remianing -= 1
    player_1_choice = input(f"Guess a number between {a} and {b}\n")
    
    if Lives_remianing<1:
        print("You Losed")
        break
    if int(player_1_choice) == rand_n:
        print(f"Correct! trials taken - {Guess_1}")
        break
    if int(player_1_choice)<rand_n:
        print("Greater number")
    elif int(player_1_choice)>rand_n:
        print("Smaller number")

Lives_remianing+=10
rand_n = random.randint(a, b)
print(f"Player 2: \n\n")

while player_2_choice!=rand_n:
    Guess_2 += 1
    Lives_remianing -= 1
    player_2_choice = input(f"Guess a number between {a} and {b}\n")
    if Lives_remianing<1:
        print("You Losed")
        break
    if int(player_2_choice) == rand_n:
        print(f"Correct! trials taken - {Guess_2}")
        break
    if int(player_2_choice)<rand_n:
        print("Greater number")
    elif int(player_2_choice)>rand_n:
        print("Smaller number")
if Guess_1>Guess_2:
    print("Player 2 wins")
elif Guess_2>Guess_1:
    print("Player 1 wins")
else: print("This game is tied with a rope")
