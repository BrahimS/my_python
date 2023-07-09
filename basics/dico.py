# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

# Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Print the "brand" value of the dictionary:
dict_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("dict_1: ", dict_1)
print("brand: ", dict_1["brand"])

# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove 
# items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# Duplicate values will overwrite existing values:

dict_2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(dict_2) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

# String, int, boolean, and list data types:
dict_3 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print("dict_3:", dict_3) #{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

# Using the dict() method to make a dictionary:
dict_4 = dict(name = "John", age = 36, country = "Norway")
print("dict_4: ", dict_4)

# Accessing Items
# You can access the items of a dictionary by 
# referring to its key name, inside square brackets:

# Get the value of the "model" key:
dict_5 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('dict_5: ', type(dict_5));
x = dict_5["model"]
print('x: ', x);  # Mustang

# There is also a method called get() that will give you the same result:

# Get the value of the "model" key:
xx = dict_5.get("brand")
print('xx: ', xx); # Ford

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

get_keys = dict_5.keys()
print('get_keys: ', get_keys); # dict_keys(['brand', 'model', 'year'])


# Get Values
# The values() method will return a list of all the values in the dictionary.


# Get a list of the values:
dict_5_value = dict_5.values()
print('dict_5_value: ', dict_5_value);  # dict_values(['Ford', 'Mustang', 1964])
print(type(dict_5_value))

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

# Get a list of the key:value pairs
dict_5_items = dict_5.items()
print('dict_5_items: ', dict_5_items); # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

dict_6 = {
  "brand": "namX",
  "model": "v1",
  "year": 2023
}
if "brand" in dict_6:
  print("Yes, 'brand' is one of the keys in the dict_6 dictionary")

# Change Values
# You can change the value of a specific item by referring to its key name:

# Change the "year" to 2024:
dict_6["year"] = 2024
print(dict_6.get('year'))

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

# Update the "model" of the car by using the update() method:
dict_6.update({'model': 'v2'})
print("dict_6: ", dict_6)

# Adding Items
# Adding an item to the dictionary is done by using 
# a new index key and assigning a value to it:
dict_7 = {
  "brand": "Neo",
  "model": "v1",
  "year": 2023
}
dict_7["color"] = "red"
print("dict_7: ", dict_7)

# Update Dictionary
# The update() method will update the dictionary with the 
# items from a given argument. If the item does not exist, the item will be added.

# The argument must be a dictionary, or an iterable object with key:value pairs.
dict_7.update({"color": "Green"})
dict_7.update({"price": 300000})
print("updated dict_7: ", dict_7)

# Removing Items
# There are several methods to remove items from a dictionary:

# The pop() method removes the item with the specified key name:
dict_8 = {
  "name": "Baba",
  "age": 47,
  "job": "developer",
  "hobby": "yoga"
}
dict_8.pop("hobby")
print("dict_8: ", dict_8)

# The popitem() method removes the last inserted item (
# in versions before 3.7, a random item is removed instead):
dict_9 = {
  "name": "Jaja",
  "age": 30,
  "hobby": "photography",
  "job": "barber",
}
dict_9.popitem()
print("dict_9: ", dict_9)

# The del keyword removes the item with the specified key name:
# The del keyword can also delete the dictionary completely: del dict_10
dict_10 = {
  "name": "Fafa",
  "age": 50,
  "hobby": "cinema",
  "job": "policeman",
}
del dict_10["age"]
print("dict_10: ", dict_10)

# The clear() method empties the dictionary:
dict_11 = {
  "name": "haja",
  "age": 70,
  "hobby": "stamps collection",
  "job": "fisherman",
}
dict_11.clear()
print("dict_11: ", dict_11)


# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of 
# the dictionary, but there are methods to return the values as well.

# print all key names in the dictionary, one by one:
dict_12 = {
  "name": "Zaza",
  "age": 49,
  "hobby": "sport",
  "job": "fireman",
}
for x in dict_12:
  print(x) # name age hobby job
# You can use the keys() method to return the keys of a dictionary:
for x in dict_12.keys():
  print(x) # name age hobby job

# Print all values in the dictionary, one by one:
for x in dict_12:
  print(dict_12[x]) # Zaza 49 sport fireman
# You can also use the values() method to return values of a dictionary:
for x in dict_12.values():
  print(x) # Zaza 49 sport fireman

# Loop through both keys and values, by using the items() method:
for x, y in dict_12.items():
  print(x, y)
# name Zaza
# age 49
# hobby sport
# job fireman

# Copy Dictionaries
# You cannot copy a dictionary simply by typing dict2 = dict1, 
# because: dict2 will only be a reference to dict1, and changes made in dict1 will a
# utomatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
dict_13 = dict_12.copy()
print('dict_13: ', dict_13);

# Make a copy of a dictionary with the dict() function:
dict_14 = dict(dict_8)
print('dict_14: ', dict_14);

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

# Create a dictionary that contain three dictionaries:
family_1 = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print('family_1: ', family_1);

# Or, if you want to add three dictionaries into a new dictionary:
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

family_2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print('family_2: ', family_2);

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, 
# starting with the outer dictionary:
print(family_2["child2"]["name"]) # Tobias

# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
