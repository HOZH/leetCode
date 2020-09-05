s = "()())()(("

l,r =0,0
for ch in s:
    l+=ch=='('
    if l==0:
        r+=ch==')'
    else:
        l-=ch==')'
print(l,r)
