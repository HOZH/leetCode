
from functools import reduce
a= int(reduce(lambda x, y: int(x)+int(y), [1,1,3]))
print(a)