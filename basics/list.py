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

# Access Items
# List items are indexed and you can access them by referring to the index number:

# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # "banana"

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.
# Return the third, fourth, and fifth item:

list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
new_list = list[2:5]
print("new_list: ", new_list) # new_list:  ['cherry', 'orange', 'kiwi']
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("my_list: ", my_list[-4:-1]) # my_list:  ['orange', 'kiwi', 'melon']

# Change Item Value
# To change the value of a specific item, refer to the index number:

# Change the second item:
the_list = ["apple", "banana", "cherry"]
the_list[1] = "blackcurrant"
print(the_list) #["apple", "blackcurrant", "cherry"]

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, 
# and refer to the range of index numbers where you want to insert the new values:

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

list_1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list_1[1:3] = ["blackcurrant", "watermelon"]
print(list_1) # ["apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango"]
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# Change the second and third value by replacing it with one value:

list_2 = ["apple", "banana", "cherry"]
list_2[1:3] = ["watermelon"]
print(list_2) # ["apple", "bwatermelon"]

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

# Insert "watermelon" as the third item:

list_3 = ["apple", "banana", "cherry"]
list_3.insert(2, "watermelon")
print(list_3) # ["apple", "banana", "watermelon", "cherry"]

# Append Items
# To add an item to the end of the list, use the append() method:
# Using the append() method to append an item:

list_4 = ["apple", "banana", "cherry"]
list_4.append("orange")
print(list_4) # ["apple", "banana", "cherry", "orange"]

# Extend List
# To append elements from another list to the current list, use the extend() method.

# Add the elements of tropical to list_5:

list_5 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
list_5.extend(tropical)
print(list_5) # ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]

# Remove Specified Item
# The remove() method removes the specified item.

# Remove "banana":
list_6 = ["apple", "banana", "cherry"]
list_6.remove("banana")
print(list_6) #["apple", "cherry"]

# Remove Specified Index
# The pop() method removes the specified index.

# Remove the third item:
list_7 = ["apple", "banana", "cherry"]
list_7.pop(2)
print(list_7) # ["apple", "banana"]
# If you do not specify the index, the pop() method removes the last item.

# The del keyword also removes the specified index:
# Remove the first item:
list_8 = ["apple", "banana", "cherry"]
del list_8[0]
print(list_8) # ["banana", "cherry"]

# The del keyword can also delete the list completely.
# Delete the entire list:
list_9 = ["apple", "banana", "cherry"]
del list_9

# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.
# Clear the list content:
list_10 = ["apple", "banana", "cherry"]
list_10.clear()
print(list_10) # []

