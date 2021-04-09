#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#

# @lc code=start
from heapq import heappop, heappush


class OrderedStream:

    def __init__(self, n: int):

        self.stream = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:

        self.stream[idKey] = value

        ans = []

        for i in range(self.ptr, 1001):
            if i in self.stream:
                ans.append(self.stream[i])
                self.ptr += 1
            else:
                return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end
