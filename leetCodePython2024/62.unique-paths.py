#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if i != 1 or j != 1:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                    
        return dp[-1][-1]




# @lc code=end
