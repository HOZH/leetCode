#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:

        # @lru_cache(None)
        # def helper(steps):
        #     if steps <= 1:
        #         return 1
        #     return helper(steps-1)+helper(steps-2)
        # return helper(n)

        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]


# @lc code=end
