#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # dp = [0]*(len(cost)+1)

        # for i in range(2, len(cost)+1):
        #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        # return dp[-1]
        # if len(cost)<1:
        #     return 0
        # if len(cost)<2:
        #     return cost[1]
        one_back,two_back = 0,0
        for i in range(2,len(cost)+1):
            temp = min(one_back+cost[i-1],two_back+cost[i-2])
            two_back=one_back
            one_back=temp
        
        return temp


# @lc code=end
