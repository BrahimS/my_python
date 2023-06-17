import time
import math

# built in functions
numbers = [1, 2, 3, 4, 5, 6, 7]

# min and max
min_number = min(numbers)
max_number = max(numbers)
print(min_number)
print(max_number)

# abs
negative_number = -100
positive_number = abs(negative_number)
print(positive_number)

# pow
def get_power_number(number_1, number_2):
    print(f"the power of {number_1} in {pow(number_1, number_2)}")

get_power_number(15, 3)


def interval_print(seconds: int):
    name = str(input('What is your name: '))
    print('Your name is ....')
    time.sleep(seconds)
    print('Your name is: ' + (name).upper())

interval_print(3)