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

#The break Statement
#With the break statement we can stop the loop even if the while condition is true:
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

