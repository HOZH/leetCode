#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        psn = []
        for i in range(1, len(dp)):
            if sqrt(i).is_integer():
                dp[i] = 1
                psn.append(i)
            else:
                for j in psn:
                    dp[i] = min(dp[i], 1+dp[i-j])

        return dp[n]

# @lc code=end
