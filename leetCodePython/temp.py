from collections import Counter,deque


s='abbc'

a=s[1:3]
print(a)
print(set(s))


d= deque([1])
# d+=2


import random
a=[1,2,3,4]

# random.shuffle(a)
print(random.sample(a,len(a)))
print(a)