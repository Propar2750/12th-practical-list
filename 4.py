"""
Data can be represented in memory in different ways Binary, Decimal, Octal and Hexadecimal. 
Input number in decimal and desired type (Specify B for binary, O for Octal, H for Hexadecimal for output. 
Write a user defined function to perform the conversions-(Do not use built in functions)
"""

dec_number = int(input("Please enter the number: "))
num_type = input("Please enter the type of number \nb: binary\no: octal\nh: hexadecimal\nEnter here: ").lower()
if num_type == 'b':
    num_type = 2
elif num_type == 'o':
    num_type = 8
elif num_type == 'h':
    num_type = 16


def count(n, r):
    x = 0
    while n // (r ** x) != 0:
        x = x + 1
    return x


def digits(n, r):
    x = count(n, r)
    digit_list = []
    while x >= 1:
        digit_list.append(str(n // (r ** (x - 1))))
        n -= (r ** (x - 1)) * (n // (r ** (x - 1)))
        x -= 1
    ans = ''.join(digit_list)
    return ans


print(digits(dec_number, num_type))

'''
Output:

Please enter the number: 10
Please enter the type of number 
b: binary
o: octal
h: hexadecimal
Enter here: o
12
'''
