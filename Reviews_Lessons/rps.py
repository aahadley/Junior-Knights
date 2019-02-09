import random

moves = ["rock", "paper", "scissors", "quit"]
win = "You win!"
lose = "You lose!"

user_score = 0
comp_score = 0

while True:

    user_move = input("Make your move.\n\t")

    if user_move == "quit":
        print("Goodbye!")
        break

    comp_move = moves[random.randint(0,2)]

    print("Computer chooses", comp_move, "\n")

    if user_move not in moves:
        print("invalid move")
        continue

    if user_move == comp_move:
        print("Tie!")

    elif user_move == "rock" and comp_move == "scissors":
        user_score += 1
        print(win)

    elif user_move == "paper" and comp_move == "rock":
        user_score += 1
        print(win)     
    
    elif user_move == "scissors" and comp_move == "paper":
        user_score += 1 
        print(win)

    else:
        comp_score += 1
        print(lose) 

    print("\n")
    print("You:", user_score, sep='\t\t')
    print("Computer:", comp_score, sep='\t')
    print("\n")