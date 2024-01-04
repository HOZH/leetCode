#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens, odds = [], []
        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        return evens+odds

# @lc code=end
