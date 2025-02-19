#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:


    def maxProfit(self,prices):
        if not prices:  # Check if the 'prices' list is empty.
            return 0  # If empty, no profit can be made, so return 0.

        # dp1[i] stores the maximum profit achievable with 1 transaction up to day i.
        dp1 = [0] * len(prices)
        # dp2[i] stores the maximum profit achievable with 2 transactions up to day i.
        dp2 = [0] * len(prices)

        # Initialize min_price as the price of the stock on the first day.
        min_price = prices[0]
        for i in range(1, len(prices)):  # Start iterating from the second day.
            # Track the minimum price encountered up to day i.
            min_price = min(min_price, prices[i])
            # Calculate the maximum profit achievable up to day i by selling at day i.
            dp1[i] = max(dp1[i-1], prices[i] - min_price)

        # Initialize max_price as the price of the stock on the last day.
        max_price = prices[-1]
        # Iterate backward from the second last day to the first day.
        for i in range(len(prices)-2, -1, -1):
            # Track the maximum price encountered from day i to the last day.
            max_price = max(max_price, prices[i])
            # Calculate the maximum profit achievable with 2 transactions by combining the profit of first and second transactions.
            dp2[i] = max(dp2[i+1], max_price - prices[i] + dp1[i])

        # The answer will be stored in dp2[0], as it represents the maximum profit achievable with 2 transactions up to the first day.
        return dp2[0]

    
# @lc code=end

