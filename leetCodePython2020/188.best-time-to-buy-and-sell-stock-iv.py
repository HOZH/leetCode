#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[[0,0] for _ in range(k + 1)] for _ in range(n + 1)]
        for day in range(n-1,-1, -1):
            for transactions in range(1,k + 1):
                for holding in range(2):
                    do_nothing = dp[day + 1][transactions][holding]
                    if holding:
                        do_something = (prices[day] + dp[day + 1][transactions - 1][0])
                    else:
                        do_something = -prices[day] + dp[day + 1][transactions][1]

                    dp[day][transactions][holding] = max(do_nothing,do_something)

        return max(dp[0])[0]







        
# @lc code=end

