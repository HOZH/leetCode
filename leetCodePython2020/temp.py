




from collections import defaultdict


d = defaultdict(int)
paragraph = "Bob hit a ball the hit BALL flew far after it was hit."
for p in "!?',,,;.":

    paragraph = paragraph.replace(p, '')
    
print(paragraph)
paragraph = paragraph.lower().split()


print(paragraph)
print(paragraph[3],paragraph[6],paragraph[3]==paragraph[6])

d['a']+=1
d['ab'[0]]+=1

print(d)
