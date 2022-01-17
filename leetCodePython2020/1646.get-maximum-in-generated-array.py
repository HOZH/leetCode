#
# @lc app=leetcode id=1646 lang=python3
#
# [1646] Get Maximum in Generated Array
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0]*(n+1)
        dp[0], dp[1] = 0, 1

        for i in range(2, n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2]+dp[i//2+1]
        return max(dp)
# @lc code=end
