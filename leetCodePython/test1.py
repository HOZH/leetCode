words = ["cat", "bb", "hat", "tree"]

chars = "atach"



# all( i for i in words[0] in chars)


a=(1,1,1)

print(all(i == 1 for i in a))

print( all( i in chars for i in words[0]))
print(all(i for i in words[1]) == "b")

# print( chars.__contains__(all(i ==for i in words[1])))


print("c" in "cat")


from collections import Counter


a= Counter("abbc")

print(a)

print(a["a"])
print(a["d"])


dic1 = dict()


dic2=dic1.copy()


dic2[1]=33

print(dic1,dic2)


from collections import *


a=(1,1,2,3,3,3)

c= Counter(a)

print(c)
print(c.values())
print(list(c.elements()))
print(list(c.items()))



A=["word","wo"]
length = len(min(A, key=lambda x: len(x)))

print(length)


a="abc"

a=[1,2,3,2]

list(set(filter( lambda x:a.count(x)==2,a)))