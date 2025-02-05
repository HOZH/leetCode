#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
from functools import lru_cache


class Solution:
    def tribonacci(self, n: int) -> int:

        @lru_cache(None)
        def helper(steps):
            if steps == 0:
                return 0
            if steps <= 2:
                return 1
            return helper(steps-1)+helper(steps-2)+helper(steps-3)

        return helper(n)

# @lc code=end
