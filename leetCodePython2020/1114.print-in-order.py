#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start
import threading
class Foo:
    def __init__(self):
        self.first_event = threading.Event()
        self.sec_event = threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_event.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_event.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.sec_event.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.sec_event.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
# @lc code=end

