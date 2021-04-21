#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
from functools import reduce


class Solution:
    def arraySign(self, nums: List[int]) -> int:

        return reduce(lambda a, b: a*b, map(lambda x: 0 if x == 0 else 1 if x > 0 else -1, nums))

# @lc code=end
