#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(lambda x: int(x), [*str(n)]))
        return reduce(lambda x, y: x*y, digits)-reduce(lambda x, y: x+y, digits)

# @lc code=end
