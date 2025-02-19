# class FooBase(object):
#     def foo(self): pass


# class A(FooBase):
#     def foo(self):
#         super().foo()
#         print( 'A.foo()')


# class B(FooBase):
#     def foo(self):
#         super().foo()
#         print( 'B.foo()')


# class C( B,A):
#     def foo(self):
#         super().foo()
#         print('C.foo()')


# class D(A):
#     def foo(self):
#         super().foo()
#         print('D.foo()')


# C().foo()
# D().foo()

# class A:
#     def foo(self):
#         print("A's foo")


# class B:
#     def foo(self):
#         print("B's foo")


# class C(A, B):
#     def foo(self):
#         # super(A, self).foo()  # Calls A's foo only
#         B.foo(self)


# c = C()
# c.foo()

from enum import Enum
class A:
    def foo(self):
        print("A's foo")


class B:
    def foo(self):
        print("B's foo")


class C(A, B):
    def foo(self):
        print("C's foo")
        super(C, self).foo()  # Calls A.foo() due to MRO


c = C()
c.foo()


class D:
    __v4 = 4
    def __init__(self):
        self.v1 = 1
        self._v2=2
        self.__v3=3
    def get_v3(self):
        return self.__v3
    def get_v4(self):
        return (self.__v4)

d =  D()
print(d.v1)
print(d._v2)
print(d.get_v3())
print(d.get_v4())


def foo(fn):
    fn('1234')

def bar(v):
    print(v+'5')

foo(bar)


# A simple decorator function
def decorator1(func):

    def wrapper1():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper1

# Applying the decorator to a function


@decorator1
def greet():
    print("Hello, World!")


greet()


# class syntax

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.value)
print(Color.RED==1)
