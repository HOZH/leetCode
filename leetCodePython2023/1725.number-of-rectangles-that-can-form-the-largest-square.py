#
# @lc app=leetcode id=1725 lang=python3
#
# [1725] Number Of Rectangles That Can Form The Largest Square
#

# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len, result = 0, 0
        for l, w in rectangles:
            local_max = min(l, w)
            if local_max > max_len:
                result = 1
                max_len = local_max
            elif local_max == max_len:
                result += 1

        return result

# @lc code=end
