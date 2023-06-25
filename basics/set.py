# Set
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.

# Sets are written with curly brackets.

# Create a Set:

set_1 = {"apple", "banana"}
print("set_1: ", set_1) #{"apple", "banana", "cherry"}
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be 
# referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items 
# after the set has been created.

# Once a set is created, you cannot change its items, but you can remove 
# items and add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# Duplicate values will be ignored:
set_2 = {"apple", "banana", "cherry", "apple"}
print("set_2: ", set_2) # {"apple", "banana", "cherry"}
print("set_2 len: ",  len(set_2)) 

# Note: The values True and 1 are considered the same value in sets, 
# and are treated as duplicates:

# True and 1 is considered the same value:
set_3 = {"apple", "banana", "cherry", True, 1, 2}
print("set_3: ", set_3)


# Set Items - Data Types
# Set items can be of any data type:

# String, int and boolean data types:
set_4 = {"apple", "banana", "cherry"}
set_5 = {1, 5, 7, 9, 3}
set_6 = {True, False, False}

# A set can contain different data types:

# A set with strings, integers and boolean values:
set_7 = {"abc", 34, True, 40, "male"}

# The set() Constructor
# It is also possible to use the set() constructor to make a set.

# Using the set() constructor to make a set:
set_8 = set(("apple", "banana", "cherry")) # note the double round-brackets
print("set_8: ", set_8)

# Access Items
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value 
# is present in a set, by using the in keyword.

# Loop through the set, and print the values:
set_9 = {"apple", "banana", "cherry"}
for x in set_9:
  print(x)

# Check if "banana" is present in the set:

set_10 = {"apple", "banana", "cherry"}
print("banana" in set_10)

# Add Items
# Once a  set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

# Add an item to a set, using the add() method:
set_11 = {"apple", "banana", "cherry"}
set_11.add("orange")
print("set_11: ", set_11)

# Add Sets
# To add items from another set into the current set, use the update() method.

# Add elements from tropical into thisset:
set_12 = {"apple", "banana", "cherry"}
set_13 = {"pineapple", "mango", "papaya"}
set_14 = set_12.update(set_13)
print("set_14: ", set_14)

# Add Any Iterable
# The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).

# Add elements of a list to at set:
set_11 = {"apple", "banana", "cherry"}
list_1 = ["kiwi", "orange"]
set_and_list = set_11.update(list_1)
print("set_and_list: ", set_11)
tuple_1 = ("Bread", 1, True, False, 200)
set_and_tuple = set_11.update(tuple_1)
print("set_and_tuple: ", set_11)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

# Remove "banana" by using the remove() method:
list_12 = {"apple", "banana", "cherry"}
list_12.remove("banana")
print("list_12: ", list_12)
# Note: If the item to remove does not exist, remove() will raise an error.
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove a 
# random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.

# Remove a random item by using the pop() method:
list_13 = {"apple", "banana", "cherry"}
x = list_13.pop()
print(x) #  apple
print("list_13: ", list_13) #  {'cherry', 'banana'}

# The clear() method empties the set:
set_15 = {"apple", "banana", "cherry"}
set_15.clear()
print("set_15: ", set_15) # set()

# The del keyword will delete the set completely:
set_16 = {"apple", "banana", "cherry"}
del set_16
# print("set_16: ", set_16) # NameError: name 'set_16' is not defined

# Loop Items
# You can loop through the set items by using a for loop:

# Loop through the set, and print the values:
set_17 = {"apple", "banana", "cherry"}
for x in set_17:
  print(x)

# Join Two Sets
# There are several ways to join two or more sets in Python.

# You can use the union() method that returns a new set containing all items 
# from both sets, or the update() method that inserts all the items from 
# one set into another:

# The union() method returns a new set with all items from both sets:
set_18 = {"a", "b" , "c"}
set_19 = {1, 2, 3}
set_20 = set_18.union(set_19)
print("set_20: ", set_20)
# Note: Both union() and update() will exclude any duplicate items.

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.

# Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) # {"apple"}

# The intersection() method will return a new set, that only contains the items that are 
# present in both sets.

# Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) # {"apple"}

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT 
# present in both sets.

# Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) # {"banana", "cherry", google", "microsoft"}

# The symmetric_difference() method will return a new set, that contains only t
# he elements that are NOT present in both sets.

# Return a set that contains all items from both sets, except items that a
# re present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) # {"banana", "cherry", google", "microsoft"}

# Set Methods
# Python has a set of built-in methods that you can use on sets.

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others