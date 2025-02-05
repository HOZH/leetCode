#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # @lru_cache(None)
        # def helper(steps):
        #     if steps <= 1:
        #         return 0
        #     return min(helper(steps-1)+cost[steps-1], helper(steps-2)+cost[steps-2])

        # return helper(len(cost))
    
        dp = [float('inf')]*(len(cost)+1)
        dp[0],dp[1] = 0,0
        for i in range(2,len(dp)):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[-1]
        
# @lc code=end

