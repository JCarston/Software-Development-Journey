# Common Types of Errors
# SyntaxError
    # Occurs when Python encounters incorrect syntax
# NameError
    # Occurs when a variable is not defined
# TypeError
    # Occurs when:
        # An operation or function is applied to the wrong tyoe
        # Python cannot intepret an operation on two objects
# IndexError
    # Occurs when you try to access an element in a list using an invalid index
# ValueError
    # Occurs when a built-in operation or function recieves an arg that has the right type but an inappropriate valie
# KeyError
    # Occurs when a dictionary does not have a specific key
# AttributeError
    # Occurs when a variable does not have an attribute


# Raise your own Exception
# Syntax
# raise ValueError("Invalid Value")
def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(color) is not str:
        raise TypeError("Color must be a string")
    if type(text) is not str:
        raise TypeError("Text must be a string")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")
colorize("hello", "red")

#Handle Errors / Try and Except Blocks
#Basic Syntax:
# try:
#     foobar
# except NameError:
#     print("You tried to use a variable that was never declared!")
# print("after the try")
#You should be as specific as possible

d = {"name": "Ricky"}
def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
    
#Try/Except/Else/Finally
while True:
    try:
        num = int(input("Please enter a number: "))
    except:
        print("That's not a number") #Runs if there is an error in the try block
    else:
        print("Good job, you entered a number") #Runs if the except doesn't
        break
    finally:
        print("RUNS NO MATTER WHAT!") #Runs no matter what

