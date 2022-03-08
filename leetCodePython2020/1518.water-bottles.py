#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        result = empty_bottles = numBottles

        while empty_bottles >= numExchange:
            temp = empty_bottles//numExchange
            empty_bottles -= temp*numExchange
            result += temp
            empty_bottles += temp
        return result

# @lc code=end
