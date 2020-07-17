import functools


@functools.lru_cache(None)
def foo(n):
    return 1

a= set([1])
print(a)
a.remove(2)