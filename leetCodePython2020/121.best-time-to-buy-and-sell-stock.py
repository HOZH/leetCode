#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # base on when to buy
        # current_max = 0
        # result = 0
        # for i in range(len(prices)-1, -1, -1):
        #     current = current_max-prices[i]
        #     result = result if current < result else current
        #     current_max = max(prices[i], current_max)
        # return result

        # base on when to sell
        # current_min = 10**8
        # result = 0
        # for i in range(len(prices)):
        #     current = prices[i] - current_min
        #     result = result if current < result else current
        #     current_min = min(current_min, prices[i])
        # return result

        # reduce prices to prices diff and then find max subarray sum-> lc 53
        if len(prices) < 2:
            return 0
        diffs = []
        for i in range(len(prices)-1):
            diffs.append(prices[i+1]-prices[i])
        dp = [0]*len(diffs)
        dp[0] = diffs[0]
        for i in range(1, len(diffs)):
            # dp[i] = max(diffs[i], dp[i-1]+diffs[i])
            dp[i] = diffs[i]+max(dp[i-1], 0)

        return max(max(dp), 0)

        # @lc code=end
