#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        diffs = []
        for i in range(len(prices)-1):
            diffs.append(prices[i+1]-prices[i])

        return sum(list(filter(lambda x: x > 0, diffs)))


# @lc code=end
