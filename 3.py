"""
Roman numerals are represented by seven different symbols I,V,X,L,C,D,M
For example 2 is written as ii in roman numeral just two one's added together. 12 is written as XII which is X + II the number 27 is written as XXVII, which is XX+V+II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for is not IIII. Instead the number four is written as IV. Because the one is before the five we subtract it making four the same principles applies to number nine which is written as IX. There are six instance where subtraction is used
-->I can be placed before V(5) and X(10) to make 4 and 9
-->X can be placed before L(5) and C(100) to make 40 and 90
-->C can be placed before D(500) and M(1000) to make 400 and 900
Write a User Defined Function which takes a string(Roman Numeral as an argument and returns the integer equivalent.

def romanToInt(s):
    return Ans

"""
input_r = list(input("Please enter the roman number: ")[::-1])
def roman_to_int(input_roman):
    roman_conversion = {'I':1,
                        'V':5,
                        'X':10,
                        'L':50,
                        'C':100,
                        'D':500,
                        'M':1000}


    number = 0
    # i goes from 0  to len - 1
    for i in range(0,len(input_roman)):
        y = roman_conversion[input_roman[i].upper()]
        if i == 0 :
            number+= y
        if i >=1:
            if roman_conversion[input_roman[i-1].upper()]>y:
                number -= y
            else:
                number+= y
    return number

print(roman_to_int(input_r))

'''
Output 1:
Please enter the roman number: LVIII
58

Output 2:
Please enter the roman number: MCMXCIV
1994
'''
