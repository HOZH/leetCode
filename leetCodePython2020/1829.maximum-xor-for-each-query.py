#
# @lc app=leetcode id=1829 lang=python3
#
# [1829] Maximum XOR for Each Query
#

# @lc code=start
from functools import reduce


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        k = (1 << maximumBit)-1
        current = reduce(lambda a, b: a ^ b, nums)

        res = [current]

        while len(nums) > 1:

            tail = nums.pop()

            current = current ^ tail
            res.append(current)

        return list(map(lambda x: x ^ k, res))


# @lc code=end
