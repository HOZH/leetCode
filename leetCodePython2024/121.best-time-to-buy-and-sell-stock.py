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
        # prices diffs when we sell on day i after bought on day i-1, so diffs[i] = prices[i] - prices[i-1]
        diffs = []
        for i in range(len(prices)-1):
            diffs.append(prices[i+1]-prices[i])

    
        # bought one day 1 and sell on day 3 = bought on day 1 and sell on day 2, then bought on day 2 and sell on day 3

        # dp[i] = max profit if we sell on day i
        # dp[i] = max of the following two:
        # 1). we bought on day i-1 and sell on day i, so dp[i] = diffs[i]
        # 2). we bought on a day before i-1 and sell on day i, so dp[i] = dp[i-1]+diffs[i]
        # bc for example [7,1,5,3,6,4], dp[3](sell on day 5) is dp[2](max profit of day 4) + diffs[3](profit of selling on day 5 rather then day 4 => 6-3) 
        # diffs = [-6, 4, -2, 3, -2]
        # dp = [-6, 4, 2, 5, 3]
        # dp[0] = -6 -> max profit for sell on day 2. This can only bought on day 1 and sell on day 2(0 indexed)
        # dp[1] = max(0,-6)+4 = -2 -> either bought on day 2 then sell on day 3, or bought on day 1 then sell on day 3
        # bought on day 1 -> profit is -6(same as bought on day 1 and sell on day 2) + 4(means bought on day 2 again(-1) + sell on day 3(+5))
        # dp[2] = max(0,4)+(-2) = 2
        # dp[3] = max(0,2)+3 = 5
        # dp[4] = max(0,5)+(-2) = 3
        # max(dp) = dp[3] = 5


        dp = [float('-inf')]*len(diffs)
        dp[0] = diffs[0]

        for i in range(1, len(diffs)):
            dp[i] = max(0, dp[i-1])+diffs[i]

        return max(0, max(dp))
    
        # max_profit = 0
        # # index, price
        # min_price = float('inf') # 32-bit, 2147....
        # # prices = [7,1,5,3,6,4]

        # i = 0 # 1, 2, 3, 4, 5
        # while i < len(prices):
        #     min_price = min(min_price, prices[i]) # (2147..., 7) -> 7; (7, 1) -> 1, (1, 5) -> 1, (1, 3) -> 1, (6, 1) -> 1, (4 , 1) -> 1
        #     max_profit = max(max_profit, prices[i] - min_price) # 7 - 2147 -> 0, (0, 1 - 1) -> 0, (0, 5 - 1 = 4) -> 4, (4, 3 - 1 = 2) -> 4, ...
        #     # ... (4, 6 - 1 = 5) -> 5, (5, 4 - 1 = 3) -> 5
        #     i += 1
        
        # return max_profit
    
        # best, current = float('-inf'), 0

        # for i in diffs:
        #     current = max(current+i, i)
        #     best = max(current, best)

        # return max(best, 0)

# @lc code=end
