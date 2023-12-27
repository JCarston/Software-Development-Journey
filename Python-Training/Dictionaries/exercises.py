# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] create a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
# Save it to a variable called answer.
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(0, 3)}
# or
answer = dict(zip(list1, list2))

# Given a person variable. Create a dictionary called answer, that makes each first item in each list a key and the second item a corresponding value.
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k: v for k, v in person}
# Could also do answer = dict(person) or answer = {thing[0]: thing[1] for thing in person}

# Create a dictionary with the key as a vowel in the alphabet and the value as 0.
answer = {char: 0 for char in "aeiou"}
# Could also do answer = dict.fromkeys("aeiou", 0)

# Your task is to create dictionary that maps ASCII keys to their corresponding letters.  Use a dictionary comprehension and chr()
answer = {count: chr(count) for count in range(65,91)}