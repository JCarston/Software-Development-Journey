#Creating Lists
#Key Syntax is [" ", " ", " "]
demo_list = ["a", 1, 45, True, 6.777]
#Check for amount of items in a list
len(demo_list)
#Another way to make a list
tasks = list(range(0 , 4))

#Accessing Values in a List
friends = ["Ashley", "Matt", "Michael"]
print(friends[0])

#Iterating Over Lists
numbers = [1, 2, 4 ,5]
for num in numbers:
    print(num)

numbers = [1, 2, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
    
sounds = ['super', 'cali', 'fragil', 'istic', 'expi', 'ali', 'docious']
result = ''
for s in sounds:
    result += s.upper()

#List Methods: Append, Insert, and Extend
#Append = Add an item to the end of the list
first_list = [1, 2, 3, 4, 5]
first_list.append(5)
print(first_list)

#Extend: Add to the end of a list all values passed to extend
second_list = [6, 7, 8, 9]
second_list.extend([10, 11, 12])
print(second_list)

#Insert: Insert an item at a given position
third_list = [13, 14, 15]
third_list.insert(2, 'Hi!')
#First argument is the index to insert at, 2nd argument is what you want to insert

#Clear: Remove all items from the list
fourth_list = [1, 2, 3, 4]
fourth_list.clear()
print(fourth_list)


#Pop: Remove the item at the given position in the list, and return it OR if no index is specified, removes and returns last item in the list
fifth_list = [1,2,3,4]
fifth_list.pop()
fifth_list.pop(1)

#Remove: Remove the first item from the list whose value is x. Throws a ValueError if the item is not found
sixth_list = [1,2,3,4]
sixth_list.remove(2)

#Index: Returns the index of the specified item in the list. Can also specify start and end.
numbers = [5,6,7,8,9,10]
numbers.index(6)
numbers.index(5, 2) #"Look for anything index that is 5 AFTER the index of 2"

#Count: Return the number of times x appears in the list
numbers1 = [1,2,3,4,3,2,1,4,10,2]
numbers.count(2)

#Sort: Sort the items of the list (in-place)
numbers3 = [1,8,7,6,4,9]
numbers3.sort()

#Reverse: Reverses the order of the list (in-place)
numbers2 = [1,2,3,4,5]
numbers2.reverse()
print(numbers2)

#Join: String method that is commonly used to convert lists to strings
words = ["Coding", " is", " Fun"]
' '.join(words)

#Slices
#Can also slice strings, but this is focusing on lists
#Syntax:
#some_list[start:end:step]
some_list = [1,2,3,4]
some_list[1:] #Gives the items that start at index 1 // If not given an end point, it will assume it ends at the end // exclusive
some_list[1:3] #Gives the items between index 1 and index 3 // If not given a start point, it will assume it starts from the beginning //exclusive
some_list[0:3:2] #Gives the items between index 1 and index 3 and stepping 2 places (counts every other number) // exclusive

#Reverse a list/string
string = "This is fun!"
string[::-1]

#Modifying portions of lists
numbers = [1,2,3,4,5]
numbers[1:3] = ['a','b','c']

#Swapping values
names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]
