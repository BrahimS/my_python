# Python Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword:
def my_function():
  print("Hello this is a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis:
my_function()

# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname).
# When the function is called, we pass along a first name, which is used inside the function to print the full name:
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil") # Emil Refsne
my_function("Tobias") # Tobias Refsnes
my_function("Linus") # Linus Refsnes

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# Number of Arguments
# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# This function expects 2 arguments, and gets 2 arguments:

def my_function2(fname, lname):
  print(fname + " " + lname)

my_function2("Emil", "Baba") # Emil Baba




# def greeting(time):
#     if time <= 12:
#         print('good morning')
#     if time > 13 and time < 18:
#         print('good afternoon')
#     if time > 19 and time < 20:
#         print('good evening')
#     if time > 21 and time < 24:
#         print('good night')

# greeting(21)


# def hello():
#     name = input('enter your name: ')
#     print('hello ' + name.upper())0

# hello()


# def good_number():
#     num = int(input('Enter a number betwwen 1 and 100:'))
#     if num >= 1 and num <= 100:
#         print( str(num) + ' is a wrong number' )
#     else:
#         print( str(num) +  ' is a not wrong number')

# good_number()


# for i in range(0, 101):
#     print('hello world ' + str(i))


# i = 0
# while i <= 10:
#     print('hello world ' + str(i))
#     i+= 1

# my_list = [1,2,3,4,5]
# new_list = []
# def multiply():
#     print(len(my_list))
#     for i in my_list:
#         new_list.append(i * 2)
#     print(my_list)
#     print(new_list)

# multiply()

numbers = [3,5,78,-7,48]
max_value = 0

def get_max_value_from_list(list):
    max_value = 0
    for number in list:
        if number > max_value:
            max_value = number
    return max_value
    
max_value = get_max_value_from_list(numbers)
print('the maximunm value is. ' + str(max_value))

def maximum():
    min_number = min(numbers)
    max_number = max(numbers)
    print(min_number)
    print(max_number)

maximum()