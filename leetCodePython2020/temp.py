import functools


@functools.lru_cache(None)
def foo(n):
    return 1




import heapq

from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
print(d['a'])
pass
print(123)