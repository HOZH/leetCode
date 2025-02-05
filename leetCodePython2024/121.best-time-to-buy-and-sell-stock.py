#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        diffs = []
        for i in range(len(prices)-1):
            diffs.append(prices[i+1]-prices[i])

        # best, current = float('-inf'), 0
        dp = [float('-inf')]*len(diffs)
        dp[0] = diffs[0]

        for i in range(1, len(diffs)):
            dp[i] = max(0, dp[i-1])+diffs[i]

        return max(0, max(dp))

        # for i in diffs:
        #     current = max(current+i, i)
        #     best = max(current, best)

        # return max(best, 0)

# @lc code=end
