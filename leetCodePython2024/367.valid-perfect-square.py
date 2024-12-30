#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num).is_integer()
        
# @lc code=end

