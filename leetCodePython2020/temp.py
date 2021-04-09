

def foo():
    num=0
    while num < 10:
        yield num
        num += 1

def bar():

    num = 0
    yield from range(0,10)


print(list(foo()))

print(list(bar()))
