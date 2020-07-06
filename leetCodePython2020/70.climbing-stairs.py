#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 2:
            return n

        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):

            dp[i] = dp[i-1]+dp[i-2]

        return dp[n]


# @lc code=end
