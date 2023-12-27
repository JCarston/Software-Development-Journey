# *args
# Special operator we can pass to functions, gathers remaining arguments as a tuple
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all_nums(4,5,6,7,8,9,10))

#**kwargs
#A special operator we can pass to functions, gathers remaining keyword arguments as a dictionary
def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']}David!"
    return "Not sure who this is..."

print(special_greeting(David="Hello "))
print(special_greeting(Bob="hello"))
print(special_greeting(David='special'))

def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

# Paremeter Ordering
# 1.parameters
# 2. *args
# 3. default parameters
# 4. **kwargs


#Tuple Unpacking
def count_sevens(*args):
    return args.count(7)
nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
result1 = count_sevens(1,4,7) #Doesn't work
result2 = count_sevens(*nums) #Unpacks the list and counts the numbers

#Dictionary Unpacking
def display_names(first,second):
    print(f"{first} says hello to {second}")
names = {"first": "Colt", "second": "Rusty"}
display_names(names) #Results in error missing a parameter
display_names(**names) #Unpacks dictionary into separate keyword arguments
