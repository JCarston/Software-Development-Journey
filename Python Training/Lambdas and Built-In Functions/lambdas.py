#Regular Function Example
def square(num):
    return num * num
print(square(9))

#Lambda function
square2 = lambda num: num * num

#Can only be one line and only a single expression
#Calling a lambda is just like calling a function
#The above example is not generally how you would create a function, you wouldn't always store it in a variable
#Generally used in place of simple single command functions that are only used once