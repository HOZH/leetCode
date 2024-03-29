#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
from functools import reduce


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        temp = []
        for i in range(n):
            temp.append(start+2*i)

        return reduce(lambda x, y: x ^ y, temp)


# @lc code=end
