#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[-1]

# @lc code=end
