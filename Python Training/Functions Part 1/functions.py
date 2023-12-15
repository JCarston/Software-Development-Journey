from random import random


#A Function is A process for executing a task that can accept input and return an output
#Structure
def name_of_function():
    #block of runnable code
    return
def say_hi():
    print('Hi!')
    
#Returning Values from Functions
#return provides an output from the function
#Exits the function
def print_square_of_7():
    return 7**2 
result = print_square_of_7()
print(result)

def coin_flip():
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"
print(coin_flip())

#Parameters
def square(num):
    return num * num
square(3)
square(8)

#default parameters
def exponent(num, power=2):
    return num ** power
#The equals in the parameters sets a default value that gets overridden if something else is passed in
#default parameters can be anything, functions, lists, dicts, strings, booleans, etc

#keyword arguments
#You can specify which parameter in the function call by using the keywords
def full_name(first, last):
    return f"Your name is {first} {last}"

full_name(last="Steele", first="Colt")

#Scope = Where our variables can be accessed
#Variables that are created in functions are scoped in that function
#Variables that are defined outside of functions are global
#You have to specify you're using a global variable within a function using global global_variable_name
#Generally a good idea to avoid global variables unless necessary

#Docstrings
#You can define a function, what it does, and the required parameters to users using """whatever"""
#Users can access it with function.__doc__