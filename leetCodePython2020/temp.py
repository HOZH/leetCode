import functools


@functools.lru_cache(None)
def foo(n):
    return 1



a = list(map(lambda x:(x[1],x),[[10,11,13],[1,50,9],[12,13,15]]))
# a= [5, 7, 9, 1, 3] 
import heapq

heapq.heapify(a)


print(type(a))
print(a)

print(heapq.heappop(a))

print(heapq.heappop(a))
import random
temp = [  random.randint(1,2) for _ in range(1000000)]
print("hola")