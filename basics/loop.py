# While Loops
# Python has two primitive loop commands:
# while loops
# for loops
# With the while loop we can execute a set of statements as long as a condition is true.
# Print i as long as i is less than 6:
a = 1
while a < 6:
    print("a:", a)
    a += 1
# The while loop requires relevant variables to be ready,
# in this example we need to define an indexing variable, i, which we set to 1.

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# Exit the loop when i is 3:
b = 1
while b < 6:
    print("b:", b)
    if b == 4:
        break
    b += 1

# The continue Statement
# With the continue statement we can stop
# the current iteration, and continue with the next:
c = 0
while c < 6:
    c += 1
    if c == 3:
        continue
    print("c:", c)

# The else Statement
# With the else statement we can run a block of code once
# when the condition no longer is true:

# Print a message once the condition is false:
d = 1
while d < 6:
    print("d:", d)
    d += 1
else:
    print("d is no longer less than 6")

# Python For Loops
#  for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages,
# and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("x:", x)
# The for loop does not require an indexing variable to set beforehand.

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:

# Loop through the letters in the word "banana":
for l in "banana":
    print("l: ", l)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

# Exit the loop when m is "banana":
fruits = ["apple", "banana", "cherry"]
for m in fruits:
  print("m:", m) # apple banana
  if m == "banana":
    break

# Exit the loop when n is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for n in fruits:
  if n == "banana": # apple
    break
  print("n:", n)

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for j in fruits:
  if j == "banana":
    continue
  print("j:", j) # apple cherry

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.

# Using the range() function:
for h in range(6):
  print("h:", h)
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# The range() function defaults to 0 as a starting value, however it is possible
# to specify the starting value by adding a parameter: range(2, 6),
# which means values from 2 to 6 (but not including 6):

# Using the start parameter:
for e in range(2, 6):
  print("e:", e)

# The range() function defaults to increment the sequence by 1, however it is possible
# to specify the increment value by adding a third parameter: range(2, 30, 3):

# Increment the sequence with 3 (default is 1):
for f in range(2, 30, 3):
  print("f:", f)  # 2 5 8 11 14 17 20 23 26 29

#  Else in For Loop
#  The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Print all numbers from 0 to 5, and print a message when the loop has ended:
for g in range(6):
  print("g:", g)
else:
  print("Finally finished!")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Break the loop when h is 4, and see what happens with the else block:
for h in range(6):
  if h == 4: break
  print("h:", h)
else:
  print("Finally finished!")

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for n in adj:
  for m in fruits:
    print("n, m:", n, m)

# The pass Statement
# for loops cannot be empty, but if you for some reason
# have a for loop with no content, put in the pass statement to avoid getting an error.
for j in [0, 1, 2]:
  pass

