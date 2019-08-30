from collections import *


# a= ""

# b= a.split()

# print(b[-1])


from collections import *

num = [1, 2, 3, 4, 5, 6, 7]
k = 3

dequeue = deque([1, 2, 3, 4, 5, 6, 7])


dequeue.rotate(k)

print(list(dequeue))


n = 10
# is_prime = [True]*n

is_prime = [ True for i in range(10)]

print(is_prime)


print(set(range(5)))




a = dict()

a[1]="A"
a[3] = "B"

for i in a :

    print(i,type(i))


print(set([1, 2]) == set([2, 1])
      )


print(set(a))

print(a.items(),a.values(),a.keys())


# from collections import *


# a= Counter((1,2,2,4))

# print(a)

# a.