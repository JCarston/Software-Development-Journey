# Screaming Repeating
times = int(input("How many times do I have to tell you? "))

for i in range(times):
    print("CLEAN YOUR ROOM")


# Unlucky Numbers
for i in range(1, 21):
    if i == 4 or i == 13:
        print(f"{i} is unlucky")
    elif i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
# Could do
for i in range(1, 21):
    if i == 4 or i == 13:
        state ="unlucky"
    elif i % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{i} is {state}")
