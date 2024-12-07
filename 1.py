"""
1. Write a program to input a number and then call the functions
count(n) which returns the numbers of digits
reverse(n) which returns the reverse of a number
has digit(n,d) which returns True if the number has d as a digit else False
show(n) to show the number in its expanded form(sum of place values of the digits in n)
(eg 124=100+20+4)
"""

input_number = int(input("Please input the number: "))


# function which returns the numbers of digits
def count(n):
    x = 0
    while n // (10 ** x) != 0:
        x = x + 1
    return x


# function which returns the reverse of a number
def reverse(n):
    return int(str(n)[::-1])


def digits(n):
    x = count(n)
    digit_list = []
    while x >= 1:
        digit_list.append(n // (10 ** (x - 1)))
        n -= (10 ** (x - 1)) * (n // (10 ** (x - 1)))
        x -= 1
    return digit_list


# function which returns True if the number has d as a digit else False
def has_digit(n, d):
    if digits(n).count(d) > 0:
        x = True
    else:
        x = False
    return x


# function to show the number in its expanded form(sum of place values of the digits in n)
def show(n):
    digits_list = digits(n)
    num_of_digits = count(n)  # or y = len(x)
    place_from_left = 0  # t will go from 0 to y
    while place_from_left < num_of_digits - 1:
        print(digits_list[place_from_left] * 10 ** (num_of_digits - 1 - place_from_left), end=" + ")
        place_from_left += 1
    print(digits_list[place_from_left] * 10 ** (num_of_digits - 1 - place_from_left))


print(count(input_number))
print(reverse(input_number))
print(has_digit(input_number, 1))
show(input_number)


""" 
Output:

Please input the number: 123456789
9
987654321
True
100000000 + 20000000 + 3000000 + 400000 + 50000 + 6000 + 700 + 80 + 9
"""
