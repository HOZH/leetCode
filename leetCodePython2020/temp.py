
from collections import Counter
temp = "aaaabbbbcccc"


counter = Counter(temp)

print(counter)
keys = sorted(counter.keys())
print(sorted(counter.keys()))

l, r = 0, len(keys)-1

# counter['a'] = 0
# counter['b'] = 0
# counter['c'] = 0

print(counter.most_common(1)[0][1])
result = ''
while counter.most_common(1)[0][1]:

    for i in range(len(keys)):

        if counter[keys[i]] != 0:
            result += keys[i]
            counter[keys[i]] -= 1

    for i in range(len(keys)-1, -1, -1):

        if counter[keys[i]] != 0:
            result += keys[i]
            counter[keys[i]] -= 1

print(result == "abccbaabccba")
