# Refactoring v1 to be cleaner

print("Rock...")
print("Paper...")
print("Scissors...")

player_one = input("Player 1, make your move: ")
player_two = input("Player 2, make your move: ")


if player_one == player_two:
    print("It's a tie!")
elif player_one == "rock":
    if player_two == "scissors":
        print("player1 wins!")
    elif player_two == "paper":
        print("player2 wins!")
elif player_one == "paper":
    if player_two == "rock":
        print("player1 wins!")
    elif player_two == "scissors":
        print("player2 wins!")
elif player_one == "scissors":
    if player_two == "rock":
        print("player2 wins")
    elif player_two == "paper":
        print("player1 wins!")
else:
    print("Something went wrong...")
