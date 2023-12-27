# Dictionaries are essentially key-value pairs, very similar to JSON format
# Example:
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    "favorite_number": 44,
}

# Accessing Individual Values
# dictionary[key]
instructor["name"]
instructor["owns_dog"]

# Iterating Dictionaries
# Use .values() for values and .keys() for keys
for value in instructor.values():
    print(value)

# Use .items() for both values and keys
instructor.items()
for key, value in instructor.items():
    print(f"key is {key} and value is {value}")

# Using In with Dictionaries
# if key in dict
if "name" in instructor:
    print("There is name key!")
if 4 in instructor.values():
    print("There is a 4 in values!")

# Clear, Copy, Fromkeys, and Get
# Clear = Clears all the keys and values in a dictionary
d = {
    "a": 1,
    "b": 2,
    "c": 3,
}

d.clear()

# Copy = Makes a copy of a dictionary
c = d.copy()

# Fromkeys = Creates key-value pairs from comma separated values
{}.fromkeys("a", "b")
{}.fromkeys(["email"], "unknown")
{}.fromkeys("a", [1, 2, 3, 4, 5])  # {a: 1,2,3,4,5}

# Get = Retrieves a key in an object and return None instead of a KeyError if the key does not exist:
d.get("a")
d.get("b")
d.get("no_key")

#############################
# Exercise
# This code picks a random food item:
from random import choice  # DON'T CHANGE!

food = choice(
    ["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"]
)  # DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25,
}
# Solution using IN
if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")
# Solution using get()
quantity = bakery_stock.get(food)
if quantity:
    print(f"{quantity} left")
else:
    print("We don't make that")

# Fromkeys Exercise
# DO NOT TOUCH game_properties!
game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements",
]

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = dict.fromkeys(game_properties, 0)
########################

# Pop, Popitems, Update
# Pop = Takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed.
d.pop("a")

# poptiem = removes a random key in a dictionary
d.popitem()

# Update = Update keys and values in a dictionary with another set of key value pairs
person = {"city": "Antigua"}
person.update(instructor)

###########Exercises################
inventory = {
    "croissant": 19,
    "bagel": 4,
    "muffin": 8,
    "cake": 1,
}  # DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list["cookie"] = 18
# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")

######################################

# Spotify Playlist Example
playlist = {
    "title": "patagonia bus",
    "author": "colt steele",
    "songs": [
        {"title": "song1", "artist": ["blue"], "duration": 2.5},
        {"title": "song2", "artist": ["kitty", "djcat"], "duration": 5.25},
        {"title": "meowmeow", "artist": ["garfield"], "duration": 2.0},
    ],
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)

#Dictionary Comprehension
#Syntax
#{__:__for__in__}
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key:value ** 2 for key,value in numbers.items()}
print(squared_numbers)