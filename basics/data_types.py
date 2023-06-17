# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:


# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# Getting the Data Type
x = 5
x_type = type(x)
print(x_type) # int

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
x = "Hello World"	# str	
x = 20	# int	
x = 20.5	# float	
x = 1j	# complex	
x = ["apple", "banana", "cherry"]	# list	
x = ("apple", "banana", "cherry")	# tuple	
x = range(6)	# range	
x = {"name" : "John", "age" : 36}	# dict	
x = {"apple", "banana", "cherry"}	# set	
x = frozenset({"apple", "banana", "cherry"})	# frozenset	
x = True	# bool	
x = b"Hello"	# bytes	
x = bytearray(5)	# bytearray	
x = memoryview(bytes(5))	# memoryview	
x = None	#NoneType	


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x) #1.0

#convert from float to int:
b = int(y) #2

#convert from int to complex:
c = complex(x) #(1+0j)
# Note: You cannot convert complex numbers into another number type.

# Random Number
# Python does not have a random() function to make a random number, 
# but Python has a built-in module called random that can be used to make random numbers:

import random
random_number = random.randrange(1, 100)
print(random_number)
print(pow(random_number, 2))

# Python Casting
# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language,
# and as such it uses classes to define data types, including its primitive types.
# Casting in python is therefore done using constructor functions:

# int() constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() constructs a string from a wide variety of data types, including strings, integer literals and float literals


# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello'  # is the same as "hello".

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

multiline_txt = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline_txt.upper())

# Boolean Values
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

# When you run a condition in an if statement, Python returns True or False:

# Print a message based on whether the condition is True or False:

num_a = 200
num_b = 33

if num_b > num_a:
  print("num_b is greater than num_a")
else:
  print("num_b is not greater than num_a")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,

# Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, 
# such as (), [], {}, "", the number 0, and the value None. 
# And of course the value False evaluates to False.

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False, and that is if you have an object 
# that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print("myobj: ", bool(myobj))

# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:

# Print the answer of a function:

def my_function() :
  return True

print("my_function: ", my_function())

# Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type:
# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))

