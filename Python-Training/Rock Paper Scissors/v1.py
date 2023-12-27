#The purpose is just to show conditionals
print("Rock...")
print("Paper...")
print("Scissors...")

player_one = input("Player 1, make your move: ")
player_two = input("Player 2, make your move: ")

if player_one == "rock" and player_two == "scissors":
    print("player 1 wins!")
elif player_one == "rock" and player_two == "paper":
    print("player2 wins!")
elif player_one == "paper" and player_two == "rock":
    print("player1 wins!")
elif player_one == "paper" and player_two == "scissors":
    print("player2 wins!")
elif player_one == "scissors" and player_two == "rock":
    print("player2 wins!")
elif player_one == "scissors" and player_two == "paper":
    print("player1 wins!")
elif player_one == player_two:
    print("It's a tie!")
else:
    print("Something went wrong...")