#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start


class Solution:
    def numSquares(self, n: int) -> int:

        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = min([dp[i-j*j]
                         for j in range(1, int(pow(i, 0.5))+1)]) + 1

        return dp[-1]

# @lc code=end
