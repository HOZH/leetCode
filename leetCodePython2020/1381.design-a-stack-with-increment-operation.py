#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#

# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):

        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:

        if len(self.stack):
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:

        if k > len(self.stack):
            self.stack = list(map(lambda x: x+val, self.stack))

        else:

            self.stack = list(
                map(lambda x: x+val, self.stack[:k]))+self.stack[k:]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end
