"""One round of Rock, Paper, Scissors. Run again for another round."""
import random

player = input("Choose rock, paper, or scissors: ").strip().lower()
computer = random.choice(["rock", "paper", "scissors"])

if player not in ["rock", "paper", "scissors"]:
    print("Please run again and choose rock, paper, or scissors.")
else:
    print("You chose", player)
    print("The computer chose", computer)
    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("The computer wins!")
