#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2, len(set(candyType)))

# @lc code=end
