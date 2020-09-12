

from collections import defaultdict


def foo(arr, t):

    l, r = 0, len(arr)-1

    while l < r:

        m = l + (r-l)//2

        current = arr[m]

        if current == t:
            return m

        elif current > t:
            r -= 1
        else:
            l += 1
    return l


print(foo([1, 2, 3,4], 4))
