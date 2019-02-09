import random

moves = ["rock", "paper", "scissors", "quit"] 
user_wins = 0
comp_wins = 0


while True:

    win = "You win! :)"
    lose = "You lose. :("

    user_move = input("Choose rock, paper, or scissors.\n\t")

    if user_move == "quit":
        break

    comp_move = moves[random.randint(0, 2)]

    print(comp_move)

    if user_move == comp_move:   
        print("Tie!")

    elif user_move == "rock" and comp_move == "scissors":
        user_wins += 1
        print(win)

    elif user_move == "paper" and comp_move == "rock":
        user_wins += 1
        print(win)

    elif user_move == "scissors" and comp_move == "paper":
        user_wins += 1
        print(win)

    else:
        comp_wins += 1
        print(lose)

    print("user score: ", user_wins)
    print("comp score: ", comp_wins)    

print("Goodbye!")