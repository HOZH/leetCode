#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.tail = self.current = Node(homepage)

    def visit(self, url: str) -> None:
        temp = Node(url)
        self.current.next = temp
        temp.prev = self.current
        self.tail = self.current = self.current.next

    def back(self, steps: int) -> str:

        while steps and self.current.prev:

            steps -= 1
            self.current = self.current.prev

        return self.current.val

    def forward(self, steps: int) -> str:

        while steps and self.current.next:

            steps -= 1
            self.current = self.current.next

        return self.current.val

        # Your BrowserHistory object will be instantiated and called as such:
        # obj = BrowserHistory(homepage)
        # obj.visit(url)
        # param_2 = obj.back(steps)
        # param_3 = obj.forward(steps)
        # @lc code=end
