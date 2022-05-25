# Paul 23.05.2022 writing FizzBuzz with odd numbers:

# 1
numbers = range(1, 101)
for number in numbers:
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)

# 2
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# 3
for i in range(1, 101):
    if i % 15 == 0:
        print(str(i) + ' is a multiple of 15 (3 and 5).')
    elif i % 5 == 0:
        print(str(i) + ' is a multiple of 5.')
    elif i % 3 == 0:
        print(str(i) + ' is a multiple of 3.')
    else:
        print(i)

# 4
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + ' is a multiple of 3 and 5 (15).')
    elif i % 5 == 0:
        print(str(i) + ' is a multiple of 5.')
    elif i % 3 == 0:
        print(str(i) + ' is a multiple of 3.')
    else:
        print(i)

# Paul 24.05.2022 in FizzBuzz for even numbers, the order of "if" statements
# will be important, for every even number is a multiple of 2, and if I put
# "if" for number 2 first, for every even number it will be True, thus
# output for 2 will be printed (always first True test in the loop will
# pass in "if-elif-else").

# 5 for even numbers
for i in range(1, 101):
    if i % 14 == 0:
        print(str(i) + ' is a multiple of 14.')
    elif i % 4 == 0:
        print(str(i) + ' is a multiple of 4.')
    elif i % 2 == 0:
        print(str(i) + ' is a multiple of 2.')
    else:
        print(i)
