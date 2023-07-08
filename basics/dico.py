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