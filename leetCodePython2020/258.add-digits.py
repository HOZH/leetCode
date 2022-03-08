#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
from functools import reduce


class Solution:
    def addDigits(self, num: int) -> int:
        temp = str(num)
        while len(temp) > 1:
            temp = str(reduce(lambda x, y: int(x)+int(y), [*temp]))
        return int(temp)

# @lc code=end
