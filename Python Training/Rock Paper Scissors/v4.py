# Introducing random computer choice
import random


# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Player 1, make your move: ").lower()
rand_num = random.randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
# player_two = input("Player 2, make your move: ")


if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("player1 wins!")
    elif computer == "paper":
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player1 wins!")
    elif computer == "scissors":
        print("computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("computer wins")
    elif computer == "paper":
        print("player1 wins!")
else:
    print("Something went wrong...")
