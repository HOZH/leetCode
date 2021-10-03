from collections import Counter

c1 = Counter('cdab')
c2 = Counter('cbad')


b = set(c1)
print(c1==c2)

counters = [c1]

for i in counters:
    if i==c2:
        print(123)
# print(c2 in b)
