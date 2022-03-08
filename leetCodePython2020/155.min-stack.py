#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
from heapq import heappush, heappop, nsmallest
from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:

        if not self.stack:
            self.stack.appendleft((x, x))
            return

        current_min = self.stack[0][1]
        self.stack.appendleft((x, min(x, current_min)))

    def pop(self) -> None:
        self.stack.popleft()

    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
