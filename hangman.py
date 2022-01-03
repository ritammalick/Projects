import random
hangman = 'Game'
para = '''once there was a boy who became bored when he watched over the village sheep grazing on the hillside to entertain himself he sang out wolf wolf the wolf is chasing the sheep
when the villagers heard the cry they came running up the hill to drive the wolf away but when they arrived they saw no wolf the boy was amused when seeing their angry faces
dont scream wolf boy warned the villagers when there is no wolf they angrily went back down the hill
later the shepherd boy cried out once again wolf wolf the wolf is chasing the sheep to his amusement he looked on as the villagers came running up the hill to scare the wolf away
as they saw there was no wolf they said strictly save your frightened cry for when there really is a wolf when there is no wolf but the boy grinned at their words while they walked grumbling down the hill once more
later the boy saw a real wolf sneaking around his flock alarmed he jumped on his feet and cried out as loud as he could wolf wolf but the villagers thought he was fooling them again and so they didn’t come to help
at sunset the villagers went looking for the boy who  returned with their sheep when they went up the hill they found him weeping
there really was a wolf here the flock is gone i cried out'''
splited = para.split(' ')
word = random.choice(splited)
# print(word)
splited_word = []
for c in range(len(word)):
    splited_word.append(word[c]) 
    # print(splited_word)
# print(splited)

splited_space = []

for i in range(len(word)):

    splited_space.append('_')
# print(splited_space)
joined_space = ' '.join(splited_space)
# print(splited_space)


# forms
form1 = '''\n
|-------|
        |
        |
        |
        |
        |
'''
form2 = '''\n
|-------|
    O   |
        |
        |
        |
        |
'''
form3 = '''\n
|-------|
    O   |
    |   |
        |
        |
        |
'''
form4 = '''\n
|-------|
    O   |
   /|   |
        |
        |
        |
'''
form5 = '''\n
|-------|
    O   |
   /|\  |
        |
        |
        |
'''
form6 = '''\n
|-------|
    O   |
   /|\  |
    |   |
        |
        |
'''
form7 = '''\n
|-------|
    O   |
   /|\  |
    |   |
   /    |
        |
'''
form8 = '''\n
|-------|
    O   |
   /|\  |
    |   |
   / \  |
        |
        |
'''

# print(form2)
# print(form1)
forms = 1
main_form = form1
print(main_form)

times = 15
for su in range(100):
    print(' '.join(splited_space))
    guess = input('Guess: ')
    
    if forms == 8:
        print("You losed hangman is fully completed")
    if guess in splited_word:
        times+=1
        splited_wo = splited_word.index(guess)
        splited_space[splited_wo] = guess
        print(' '.join(splited_space))
        
        if '_' in splited_space:
            pass
        else:
            print("You won the game")
            break
    else:
        print(' '.join(splited_space))
        forms+=1
        # print(forms)
        if forms == 1:
            main_form = form1
        elif forms == 2:
            main_form = form2
        elif forms == 3:
            main_form = form3
        elif forms == 4:
            main_form = form4
        elif forms == 5:
            main_form = form5
        elif forms == 6:
            main_form = form6
        elif forms == 7:
            main_form = form7
        elif forms == 8:
            main_form = form8
            print("You losed")
            print("the word is ", word)
            break  
    print(main_form)  


    
        