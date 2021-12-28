#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        if not len(prices):
            return 0
        # dp[i][1] holding
        # dp[i][0] empty
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # prices[i]+dp[i-1], selling
            dp[i][0] = max(prices[i]+dp[i-1][1]-fee, dp[i-1][0])
            dp[i][1] = max(-prices[i]+dp[i-1][0], dp[i-1][1])

        return dp[-1][0]


# @lc code=end
