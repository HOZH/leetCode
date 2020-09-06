#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        if n < 2:
            return 0
        dp = [0]*(n+1)
        for i in range(2, n+1):
            dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
        return dp[-1]

# @lc code=end
