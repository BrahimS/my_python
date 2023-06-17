# Python Lists
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to 
# store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

mylist = ["Beans", "Bread", "Fruits"]
print("my_list: ", mylist)
print("my_list length: ", len(mylist))
print("my_list type: ", type(mylist))

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, 
# and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in 
# a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
thislist.append("Bread")
print(thislist)