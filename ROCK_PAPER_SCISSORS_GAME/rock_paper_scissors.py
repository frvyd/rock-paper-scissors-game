#ROCK PAPER SCISSOR GAME

import random as rnd

option = ["rock" , "paper" , "scissors"]
rock = option [0]
paper = option [1]
scissors = option[2]
print("Welcome to the Rock - Paper - Scissors Game!")

tocontinue = input("Press 'q' to exit the game or any key to continue: ")
tocontinue = tocontinue.lower()
if tocontinue == "q":
    print("You're out of the game!")

while True:
    choice = input ("Rock-Paper-Scissors Choose one:")
    pc_choice = rnd.choice (option)

    if choice == pc_choice:
            print ("Choice of computer:",choice)
            print ("ENDS IN A DRAW!")
            print("#" * 60)

    if choice == rock:
        if pc_choice == paper:
            print ("Choice of computer: paper")
            print ("Paper wraps the rock. COMPUTER WINS!")
            print("#" * 60)

        elif pc_choice == scissors:
            print ("Choice of computer: scissors")
            print ("The stone breaks the scissors. YOU'RE WINNER!")
            print("#" * 60)
        else:
             continue
        
    if choice == paper:
        if pc_choice == scissors:
            print ("Choice of computer: scissors")
            print ("Scissors cut the paper. COMPUTER WINS!")
            print("#" * 60)

        elif pc_choice == rock:
            print ("Choice of computer: rock")
            print ("Paper wraps the rock. YOU'RE WINNER!")
            print("#" * 60)
        else:
             continue
        
    if choice == scissors:
        if pc_choice == rock:
            print ("Choice of computer: rock")
            print ("The stone breaks the scissors. COMPUTER WINS!")
            print("#" * 60)

        elif pc_choice == paper:
            print ("Choice of computer: scissors")
            print ("Scissors cut the paper. YOU'RE WINNER!")
            print("#" * 600)
        else:
             break
        
    if choice == "q":
        print ("You're out of the game.")
        exit()
            