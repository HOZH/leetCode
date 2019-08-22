

from collections import *
a = [1, 2, 2, 3, 3]
print(1)
print(a)
print(max(a, key=a.count))

lis = [2147483647, 1, 1, 2]


a = Counter(lis)
print(a.most_common(1)[0][1])


for i, j in enumerate(a):
    print(i, j)

# print(max(lis.count))


# print(lis)
# print(max(lis.count))


# print(list(set(filter(lambda x: x ==
#                       max(lis, key=lis.count), lis))))


# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
a = [-2, 0, 3, -5, 2, -1]

print(a[0:2+1])
print(a[2:5+1], sum(a[2:5+1]))
print(a[0:5+1], sum(a[0:5+1]))


from math import *

# a=factorial(12)
# print(a>2147483647)
# print(a)


for i in range(4,-1,-1):
    print(i)
print(factorial(25))


a=1808548329

b=a//10
print(b)

for i in range(0,99,5):
    print(i)
