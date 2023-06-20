# Tuples
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections 
# of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Create a Tuple:
tuple_1 = ("job", "age", "name", 1, True, 1.5)
print("tuple_1: ", tuple_1)

# Ordered
# When we say that tuples are ordered, it means that the 
# items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change,
# add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# Tuples allow duplicate values:
tuple_2 = ("apple", "banana", "cherry", "apple", "cherry")
print("tuple_2: ", tuple_2)

# To determine how many items a tuple has, use the len() function:

# Print the number of items in the tuple:
tuple_3 = ("apple", "banana", "cherry")
print("tuple_3: ", len(tuple_3))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# One item tuple, remember the comma:
tuple_4 = ("apple",)
print(type(tuple_4))

#NOT a tuple
tuple_4 = ("apple")
print("tuple_4:", type(tuple_4))

# Tuple Items - Data Types
# Tuple items can be of any data type:

# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:
# A tuple with strings, integers and boolean values:
tuple4 = ("abc", 34, True, 40, "male")

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

# Using the tuple() method to make a tuple:
tuple_5 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print("tuple_5:", tuple_5)

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

# Print the second item in the tuple:
tuple_6 = ("apple", "banana", "cherry")
print("tuple_6:",tuple_6[1])

# Negative Indexing
# Negative indexing means start from the end.

# -1 refers to the last item, -2 refers to the second last item etc.

# Print the last item of the tuple:
tuple_7 = ("apple", "banana", "cherry")
print("tuple_7:", tuple_7[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new tuple with the specified items.

# Return the third, fourth, and fifth item:
tuple_8 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("tuple_8:", tuple_8[2:5])
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

# Check if "apple" is present in the tuple:
tuple_9 = ("apple", "banana", "cherry")
if "apple" in tuple_9:
  print("tuple_9:", "Yes, 'apple' is in the fruits tuple")



# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.

# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, 
# dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type. 
# Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.