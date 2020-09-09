#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        rest, sold, hold = 0, 0, float('-inf')
        # rest-> from previous rest,hold
        # hold->from previous hold,sold
        # sold->from previous rest
        for i in range(len(prices)):
            prev_rest, prev_hold, prev_sold = rest, hold, sold
            hold = max(prev_hold, prev_rest-prices[i])
            sold = prev_hold+prices[i]
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)


# @lc code=end
