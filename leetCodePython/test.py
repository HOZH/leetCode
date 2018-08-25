

str1 = 'sbwanyi'
print([c for c in str1])

print(list(str1))
# [str1] doesn't convert string to chars
print(type([]))


#/usr/bin/env python
# coding:utf-8
'''
13195的质数因子有5,7,13和29.

600851475143的最大质数因子是多少？

'''
num = 6008514751


def isPrime(number):
    '''判断一个数是不是质数，如果是返回真，否则返回假'''
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def largestPrimeFactor(num):

    for m in range(int(num**0.5), 0, -1):
        if num % m == 0:
            if isPrime(m):
                return m
    return None


m = largestPrimeFactor(num)
print(m)
