import random
import money_sender as ms
import pyautogui as pg



def play_():

    score = 0
    score = int(score)
    print("INSTUCTIONS:\n type r for rock \n type p for paper\n type s for scissor")
    print()

    print()

    for i in range(5):
        comp = random.randint(1, 3)

        print(f"ROUND {i+1}")
        print()
        user = input("Enter your guess\n")
        if comp == 1:
            m = "rock"
        elif comp == 2:
            g = "paper"
        elif comp == 3:
            h = "sissor"
            #    If comp choosed r
        if user == "r" and comp == 2:
            print("You lose! computer choosed", g)
        elif user == "r"  and comp == 3:
            print("You Win! computer choosed", h)
            score = score+10
            #    If comp choosed p
        elif user =="p"  and comp == 3:
            print("You lose! computer choosed", h)
        elif user == "p"  and comp == 1:
            print("You Win! computer choosed", m)
            score = score+10
            #    If comp choosed s
        elif user == "s"  and comp == 1:
            print("You lose! computer choosed", m)
        elif user == "s"  and comp == 2:
            print("You Win! computer choosed", g)
            score = score+10
        
        else:
            tied = 0
            tied = tied+10
            print("This gami is tied")
        print()

    print()
    print("Your total score is ", score,"\n")
    comp_score= (50-tied)-score
    if comp_score>score:
        print("You Lose! Try again later\n")
    elif comp_score<score:
        print("You Win!\n")
    elif comp_score==score:
        print("The game is tie\n")
    print(f"Computer total score is {(50-tied)-score}\n")

    if score == 0:
        ms.mone(-10)
        
    elif score == 10:
        ms.mone(10)
        pg.alert('Congo! Rs 10 has been transfered to your bank account')
    elif score == 20:
        ms.mone(30)
        pg.alert('Congo! Rs 30 has been transfered to your bank account', 'Rock Paper Scissor')
    elif score == 30:
        ms.mone(50)
    elif score == 40:
        ms.mone(70)
    elif score == 50:
        ms.mone(100)

    pg.alert('Congo! Rs 10 has been transfered to your bank account')

    play_again = int(input("\n Do you want to play again?\n ('1 for yes, 2 for no')"))

    if play_again==1:
        print("ok")
        play_()
    else:
        print("Thank You for playing")
        exit()

play_()

print("Thank You for playing")

