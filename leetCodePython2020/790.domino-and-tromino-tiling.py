#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    def numTilings(self, N: int) -> int:

        kMod = 10**9+7

        dp = [[0, 0, 0] for _ in range(N+1)]
        dp[0][0] = dp[1][0] = 1

        for i in range(2, N+1):

            dp[i][0] = (dp[i-1][0]+dp[i-2][0]+dp[i-1][1]+dp[i-1][2]) % kMod
            dp[i][1] = (dp[i-2][0]+dp[i-1][2]) % kMod
            dp[i][2] = (dp[i-2][0]+dp[i-1][1]) % kMod

        return dp[-1][0]

# @lc code=end
