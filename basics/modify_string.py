# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Get the characters from position 2 to position 12 (not included):
sliced_txt = "Hello python "
print(sliced_txt[3:8])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:

# Get the characters from the start to position 5 (not included):
print(sliced_txt[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:
# Get the characters from position 5, and all the way to the end:

print(sliced_txt[5:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):

nigative_index_sliced_txt = "Hello, World!"
print(nigative_index_sliced_txt[-5:-2])

# Python - Modify Strings
# Python has a set of built-in methods that you can use on strings.

# The upper() method returns the string in upper case:
upper_case = "Hello, World!"
print(upper_case.upper())

# The lower() method returns the string in lower case:
lower_case = "HELLO, WORLD!"
print(lower_case.lower())

# The capitalize() method returns the string in capital case:
capitalize_txt = "hello, world!"
print(capitalize_txt.capitalize())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, 
# and very often you want to remove this space.

# The strip() method removes any whitespace from the beginning or the end:

no_whitespace_txt = "  remove all the white space!  "
print(no_whitespace_txt.strip())

# Replace String
# The replace() method replaces a string with another string:

replace_txt = "Hello, Toto!"
print(replace_txt.replace("o", "a")) # Hella, Tata!

# Split String
# The split() method returns a list where the text 
# between the specified separator becomes the list items.

split_txt = "salut,le,monde"
print(split_txt.split(',')) # ['salut', 'le', 'monde']
print(type(split_txt)) # String

# More string methods
# capitalize()	 Converts the first character to upper case
# casefold()	 Converts string into lower case
# center()	 Returns a centered string
# count()	 Returns the number of times a specified value occurs in a string
# print(encode(exemple))	 Returns an encoded version of the string
# endswith()	 Returns true if the string ends with the specified value
# expandtabs()	 Sets the tab size of the string
# find()	 Searches the string for a specified value and returns the position of where it was found
# format()	F ormats specified values in a string
# format_map()	 Formats specified values in a string
# index()	 Searches the string for a specified value and returns the position of where it was found
# isalnum()	 Returns True if all characters in the string are alphanumeric
# isalpha()	 Returns True if all characters in the string are in the alphabet
# isascii()	 Returns True if all characters in the string are ascii characters
# isdecimal()	 Returns True if all characters in the string are decimals
# isdigit()	 Returns True if all characters in the string are digits
# isidentifier()	 Returns True if the string is an identifier
# islower()	 Returns True if all characters in the string are lower case
# isnumeric()	 Returns True if all characters in the string are numeric
# isprintable()	 Returns True if all characters in the string are printable
# isspace()	 Returns True if all characters in the string are whitespaces
# istitle()	 Returns True if the string follows the rules of a title
# isupper()	 Returns True if all characters in the string are upper case
# join()	 Converts the elements of an iterable into a string
# ljust()	 Returns a left justified version of the string
# lower()	 Converts a string into lower case
# lstrip()	 Returns a left trim version of the string
# maketrans()	 Returns a translation table to be used in translations
# partition()	 Returns a tuple where the string is parted into three parts
# replace()	 Returns a string where a specified value is replaced with a specified value
# rfind()	 Searches the string for a specified value and returns the last position of where it was found
# rindex()	 Searches the string for a specified value and returns the last position of where it was found
# rjust()	 Returns a right justified version of the string
# rpartition()	 Returns a tuple where the string is parted into three parts
# rsplit()	 Splits the string at the specified separator, and returns a list
# rstrip()	 Returns a right trim version of the string
# split()	 Splits the string at the specified separator, and returns a list
# splitlines()	 Splits the string at line breaks and returns a list
# startswith()	 Returns true if the string starts with the specified value
# strip()	 Returns a trimmed version of the string
# swapcase()	 Swaps cases, lower case becomes upper case and vice versa
# title()	 Converts the first character of each word to upper case
# translate()	 Returns a translated string
# upper()	 Converts a string into upper case
# zfill()	 Fills the string with a specified number of 0 values at the beginning


# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

# Get your own Python Server
# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld

# Format - Strings
# As we learned in the Python Variables chapter, 
# we cannot combine strings and numbers like this:
# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
age = 36
job = 'devlopper'
txt = "My name is John, I am {} and i work as a {}"
print(txt.format(age, job))

# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters used in Python:
# \'	 Single Quote	
# \\	 Backslash	
# \n	 New Line	
# \r	 Carriage Return	
# \t	 Tab	
# \b	 Backspace	
# \f	 Form Feed	
# \ooo	 Octal value	
# \xhh	 Hex value

