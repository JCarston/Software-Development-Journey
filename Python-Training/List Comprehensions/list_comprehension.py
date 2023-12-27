# Simple syntax that lets you create lists from lists
# Syntax:
# [variable to be created for iterable item in list/range/something interable]
# Example:
nums = [1, 2, 3]
[x * 10 for x in nums]

name = "colt"
[char.upper() for char in name]

friends = ["Ashley", "Matt", "Michael"]
[friend.capitalize() for friend in friends]

[num * 10 for num in range(1, 6)]

# List Comprehension with Conditional Logic
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

[num * 2 if num % 2 == 0 else num / 2 for num in numbers]

with_vowels = "This is so much fun!"
"".join(char for char in with_vowels if char not in "aeiou")

# Exercises

# 1. Given a list of names, create a variable called answer, which is a new list containing the first letter of each name
answer = [person[0] for person in ["Elie", "Tim", "Matt"]]

# 2 Given a list of numbers, create a new variable called answer2, which is a new list of all the even values.
answer2 = [val for val in [1, 2, 3, 4, 5, 6] if val % 2 == 0]

# 3 Given two lists [1,2,3,4] and [3,4,5,6], which is a new list that is the intersection of the two. Output should be [3,4]
answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]

# 4 Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer 2, which is a new list with each word reversed and in lower case
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
# The slice [::-1] is a quick way to reverse a string

# 5 For all the numbers between 1 and 100 (inclusive), create a variable called answer, which contains a list with all the numbers that are divisible by 12.
answer = [val for val in range(1, 101) if val % 12 == 0]

# 6 Given the string "amazing", create a variable called answer, which is a list containing all the letters from "Amazing" but not the vowels.
answer = [char for char in "amazing" if char not in "aeiou"]

# Nested Lists
# Lists can contain any kid of element, even other lists
nested_list = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
# Accessing Nested lists
nested_list[0][
    1
]  # First bracket determines which list in the nested list that you want, and the 2nd bracket targets the index
nested_list[1][-1]

# printing vales in nested lists
for l in nested_list:
    for val in l:
        print(val)

# Nested List Comprehension
[[print(val) for val in l] for l in nested_list]

board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)
[["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]

# Using a nested list comprehension and range(), create a variable called answer with the following values [[0,1,2], [0,1,2], [0,1,2]]
answer = [[i for i in range(0, 3)] for num in range(0, 3)]

# Using list comprehension, create a variable called answer with the following value :

# [
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  ]
# it's a 10x10 nested list.  10 rows, each row contains the numbers 0-9.   Don't worry about the formatting/spacing, I just added a bunch of returns to make things clearer. Your answer will be all on one giant line. Use nested list comprehension and range() to accomplish this.

answer = [[i for i in range(0, 10)] for num in range(0, 10)]
