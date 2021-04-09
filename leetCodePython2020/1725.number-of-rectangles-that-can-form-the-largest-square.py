#
# @lc app=leetcode id=1725 lang=python3
#
# [1725] Number Of Rectangles That Can Form The Largest Square
#

# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:


        sides = list(map(lambda x:min(x),rectangles))

        return sides.count(max(sides))


        
# @lc code=end

