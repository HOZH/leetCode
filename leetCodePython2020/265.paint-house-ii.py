#
# @lc app=leetcode id=265 lang=python3
#
# [265] Paint House II
#

# @lc code=start
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        if not len(costs):
            return 0
        color_len = len(costs[0])

        dp = [[0]*color_len for _ in range(len(costs))]

        dp[0] = costs[0][:]

        for i in range(1, len(costs)):
            for j in range(color_len):
                temp = []
                for k in range(color_len):
                    if k != j:
                        temp.append(dp[i-1][k])

                dp[i][j] = costs[i][j]+min(temp)

        return min(dp[-1])

# @lc code=end
