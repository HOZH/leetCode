import functools


@functools.lru_cache(None)
def foo(n):
    return 1



from collections import defaultdict, OrderedDict


a= OrderedDict()
a[1]=1


print(a.values())
print(next(iter(a.items())))
