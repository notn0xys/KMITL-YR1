import random

user = int(input("Scissor(0), Rock(1), Paper(2)"))
com_gen = random.randrange(0,3)

if user == 0:
    if com_gen == 0:
        print("The computer chose scissor, player chose scissor You tie")
    elif com_gen == 1:
        print("The computer chose Rock, player chose scissor You Lose")
    else:
        print("The computer chose Paper, player chose scissor You Win")
elif user == 1:
    if com_gen == 0:
        print("The computer chose scissor, player chose Rock You Win")
    elif com_gen == 1:
        print("The computer chose Rock, player chose Rock You Tie")
    else:
        print("The computer chose Paper, player chose Rock You lose")
elif user ==2:
    if com_gen == 0:
        print("The computer chose scissor, player chose Paper You Lose")
    elif com_gen == 1:
        print("The computer chose Rock, player chose Rock You Win")
    else:
        print("The computer chose Paper, player chose Rock You Tie")
else:
    print("wrong input rawr")
    
