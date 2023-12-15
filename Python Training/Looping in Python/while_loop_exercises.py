# Simple example
msg = input("What's the secret password?")
while msg != "bananas":
    print("WRONG!")
    msg = input("What's the secret password?")
print("CORRECT!")

# Convert For Loop to While Loop
for num in range(1, 11):
    print(num)

num = 1
while num < 11:
    print(num)
    num += 1

# EXERCISE: Emoji Art
# For Loop Version
for num in range(1, 11):
    print("\U0001f600" * num)
# While Loop Version
times = 1
while times <= 10:
    print("\U0001f600" * times)
    times += 1

#EXERCISE: Stop Copying Me
response = input("Hey, how's it going? ")
while response != "stop copying me":
    print(response)
    response = input()
print("UGH FINE YOU WIN")

#Controlled Loop Exit
while True:
    command = input("Type 'exit' to exit")
    if command == "exit":
        break