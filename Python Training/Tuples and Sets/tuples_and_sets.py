# Tuple = An ordered collection or grouping of items that are immutable
# Syntax:
numbers = (1, 2, 3, 4)  # Can use other data types

# Why Use a Tuple? = They are faster than lists, makes code safer (from bugs and problems), valid keys in a dictionary

# Creating/ Accessing
# Create using() or the tuple function
# Accessing is just like a list

first_tuple = (
    1,
    2,
    3,
    3,
    3,
)
first_tuple[1] // 2
first_tuple[2] // 3

second_tuple = tuple(5, 1, 2)

# Tuple looping and methods
# same syntax as a list including for loops, while loops, slices, etc
months = ("January", "February", "March", "April", "June")
for month in months:
    print(month)
# count = Returns the number of times a vlaue appears in a tuple
first_tuple.count(3)
# index = Returns at which a value is found in a tuple
first_tuple.index(1)


# Sets = Sets are like formal mathematical sets
# Sets do not have duplicate values
# Elements in sets aren't ordered and can't be accessed by index
# Syntax
s = set({1, 4, 5})
s = {1, 4, 5}
4 in s
8 in s

for thing in s:
    print(thing)
# Common use case: Take a list and convert to a set to get unique elements (some_list(list(set)))

# add = adds an element to a set. If the element is already in the set, it doesn't change:
s.add(4)

# remove = remove a value from a set
s.remove(3)
# If you need to avoice KeyErrors use .discard() instead

# copy = Creates a copy of the set
another_s = s.copy()

# clear = Removes all the contents of the set
s.clear()

# union = combine 2 sets and keeping only unique elements, done using the | character, works as a OR, can use & to see only elements that are in both sets
# math_students | biology_students


# Exercise
# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1, 2, 3, 4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)

# 3 - Given the following variable:

values = [10, 20, 30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)

# 4 - Given the following variable

stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)


#Set Comprehension
#Same idea as list and dict comprehension

{x**2 for x in range(10)}

string = "hello"
{char for char in string if char in 'aeiou'}