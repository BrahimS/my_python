
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