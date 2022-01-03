def rock_paper_scissor():

    import random
    

    comp = random.randint(1, 3)

    score = 0
    score = int(score)
    print("INSTUCTIONS:\n type r for rock \n type p for paper\n type s for scissor")
    print()
    print(f"ROUND 1")
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
        print("This gami is tied")

    # mid lines
    print()
    print()
    print("ROUND 2")

    #Round 2

    comps = random.randint(1, 3)

    users = input("Enter your guess\n")
    if comps == 1:
        mm = "rock"
    elif comps == 2:
        gg = "paper"
    elif comps == 3:
        hh = "sissor"

    if users == "r" and comps == 2:
                        print("You lose! computer choosed", gg)
    elif users == "r"  and comps == 3:
                        print("You Win! computer choosed", hh)
                        score = score+(10*1)
    elif users =="p"  and comps == 3:
                        print("You lose! computer choosed", hh)
    elif users == "p"  and comps == 1:
                        print("You Win! computer choosed",mm)
                        score = score+10
    elif users == "s"  and comps == 1:
                        print("You lose! computer choosed", mm)
    elif users == "s"  and comps == 2:
                        print("You Win! computer choosed", gg)
                        score = score+10
    else:
                        print("This gami is tied")

    # mid lines
    print()
    print()
    print("ROUND 3")

    #Round 3

    comp3 = random.randint(1, 3)

    users = input("Enter your guess\n")
    if comp3 == 1:
        mmm = "rock"
    elif comp3 == 2:
        ggg = "paper"
    elif comp3 == 3:
        hhh = "sissor"

    if users == "r" and comp3 == 2:
                print("You lose! computer choosed", ggg)
    elif users == "r"  and comp3 == 3:
                        print("You Win! computer choosed", hhh)
                        score = score+(10*1)
    elif users =="p"  and comp3 == 3:
                        print("You lose! computer choosed", hhh)
    elif users == "p"  and comp3 == 1:
                        print("You Win! computer choosed",mmm)
                        score = score+10
    elif users == "s"  and comp3 == 1:
                        print("You lose! computer choosed", mmm)
    elif users == "s"  and comp3 == 2:
                        print("You Win! computer choosed", ggg)
                        score = score+10
    else:
                        print("This gami is tied")
                    
    # mid lines
    print()
    print()
    print("ROUND 4")

    #Round 4

    comps4 = random.randint(1, 3)

    users = input("Enter your guess\n")
    if comps4 == 1:
        mm2 = "rock"
    elif comps4 == 2:
        gg2 = "paper"
    elif comps4 == 3:
        hh2 = "sissor"

    if users == "r" and comps4 == 2:
                        print("You lose! computer choosed", gg2)
    elif users == "r"  and comps4 == 3:
                        print("You Win! computer choosed", hh2)
                        score = score+(10*1)
    elif users =="p"  and comps4 == 3:
                        print("You lose! computer choosed", hh2)
    elif users == "p"  and comps4 == 1:
                        print("You Win! computer choosed",mm2)
                        score = score+10
    elif users == "s"  and comps4 == 1:
                        print("You lose! computer choosed", mm2)
    elif users == "s"  and comps4 == 2:
                        print("You Win! computer choosed", gg2)
                        score = score+10
    else:
                        print("This gami is tied")

    # mid lines
    print()
    print()
    print("ROUND 5")

    #Round 5

    comps6 = random.randint(1, 3)

    users = input("Enter your guess\n")
    if comps6 == 1:
        mm5 = "rock"
    elif comps6 == 2:
        gg5 = "paper"
    elif comps6 == 3:
        hh5 = "sissor"

    if users == "r" and comps6 == 2:
                        print("You lose! computer choosed", gg5)
    elif users == "r"  and comps6 == 3:
                        print("You Win! computer choosed", hh5)
                        score = score+(10*1)
    elif users =="p"  and comps6 == 3:
                        print(f"You lose! computer choosed {hh5}")
    elif users == "p"  and comps6 == 1:
                        print("You Win! computer choosed",mm5)
                        score = score+10
    elif users == "s"  and comps6 == 1:
                        print("You lose! computer choosed", mm5)
    elif users == "s"  and comps6 == 2:
                        print("You Win! computer choosed", gg5)
                        score = score+10
    else:
                        print("This gami is tied")

    print()
    print("Your total score is ", score)
    print("Thank You for playing")

def perfect_guess():
    import random
    userguess = True
    Rand = random.randint(1, 50)
    score = 0
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
    