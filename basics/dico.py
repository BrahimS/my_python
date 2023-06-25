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
print("dict_3:", dict_3)

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

# Using the dict() method to make a dictionary:

dict_4 = dict(name = "John", age = 36, country = "Norway")
print("dict_4: ", dict_4)

