from collections import *




# a= ""

# b= a.split()

# print(b[-1])



from collections import *

num = [1, 2, 3, 4, 5, 6, 7]
k=3

dequeue = deque([1, 2, 3, 4, 5, 6, 7])


dequeue.rotate(k)

print(list(dequeue))


