#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = list(map(lambda x: int(x), list(str(n))))
        return reduce(lambda x, y: x*y, temp)-reduce(lambda x, y: x+y, temp)

# @lc code=end
