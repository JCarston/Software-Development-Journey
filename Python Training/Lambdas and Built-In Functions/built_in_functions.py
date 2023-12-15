#map()
#A standard function that accepts at least two arguments, a functiona and an "iterable"

nums = [2,4,6,8,10]
doubles = map(lambda x: x*2, nums)
for num in doubles:
    print(num)
#Can also convert to list with doubles = list(map(lambda x: x**2, nums))
def decrement_list(l):
    return list(map(lambda n: n-1, l))

#Filter
#Can pass in a lambda and returns only the values that return true
list1 = [1,2,3,4,5,6]
evens = list(filter(lambda x: x % 2 == 0, list1))

names = ['Lassie', 'Colt', 'Rusty']
list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) < 5, names)))
#The above maps the names list only if the name is less than 5 characters
#list comprehension version
[f"Your instructor is {name}" for name in names if len(name) <5]

#More Built-In Functions
#all() - Returns true if all elements of the iterable are truthy(or empty)
#any() - Returns true if any elements of the iterable are truthy
#sorted() - Returns a new sorted list from the items in iterable. Can reverse an interable with sorted(iterable, reverse=True). Can also pass in a key= parameter to determine how the iterable gets sorted
users = [
    {"username": "samuel"}
]
sorted(users, key=lambda user: user["username"]) #Example of sorting with a lambda as a key

#min() - Returns the smallest item in an iterable or the smallest of two or more arguments
#max() - Returns the largest item in an iterable or the largest of two or more arguments
#Can pass in a key parameter (also lambda) as well

#reversed() - Return a reverse iterator