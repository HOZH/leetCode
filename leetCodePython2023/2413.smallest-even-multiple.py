#
# @lc app=leetcode id=2413 lang=python3
#
# [2413] Smallest Even Multiple
#

# @lc code=start
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return 2*n

# @lc code=end
