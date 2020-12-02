




from functools import reduce
a=['a','b']

b= reduce(lambda a,b:a+b,a)
print(b)