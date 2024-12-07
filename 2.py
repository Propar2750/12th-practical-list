"""
A number is a perfect number if the sum of all the factors of the number including 1 excluding itself is equa l to number.

For example: 6 = 1+2+3 and 28 = 1+2+4+7+14
Number is a prime number if it's factors are 1 and itself.
Write function
i) Generatefactors() to populate a list of factors
ii) isPrimeNo() to check whethere the number is prime number or not
iii) isPerfectNo() to check whether the number is perfect number or not
"""

input_number = int(input("Please input the number: "))


def Generatefactors(n):
    factors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i != int(n / i):
                factors.extend([i, int(n / i)])
            else:
                factors.append(i)

    return factors


def isPerfectNo(n):
    total = 0
    for i in factors:
        total += i

    if total == n:
        return True
    else:
        return False


def isPrimeNo():
    if len(factors) == 1:
        return True
    else:
        return False


print(Generatefactors(input_number))
factors = Generatefactors(input_number)
print(isPerfectNo(input_number))
print(isPrimeNo())

"""
Output:

Please input the number: 2305843008139952128 
[1, 2, 1152921504069976064, 4, 576460752034988032, 8, 288230376017494016, 16, 144115188008747008, 32, 72057594004373504,
64, 36028797002186752, 128, 18014398501093376, 256, 9007199250546688, 512, 4503599625273344, 1024, 2251799812636672,
2048, 1125899906318336, 4096, 562949953159168, 8192, 281474976579584, 16384, 140737488289792, 32768, 70368744144896,
65536, 35184372072448, 131072, 17592186036224, 262144, 8796093018112, 524288, 4398046509056, 1048576, 2199023254528,
2097152, 1099511627264, 4194304, 549755813632, 8388608, 274877906816, 16777216, 137438953408, 33554432, 68719476704,
67108864, 34359738352, 134217728, 17179869176, 268435456, 8589934588, 536870912, 4294967294, 1073741824, 2147483647] 
True 
False 
"""
