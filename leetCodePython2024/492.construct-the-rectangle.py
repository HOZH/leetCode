#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
from math import sqrt, floor


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # floor 1.2 => 1, floor 1.8 => 1, floor(sqrt(50)) => 7
        # find the floor value of squre root for the input number
        # then keep doing integer division for the decreasing visivor from base number
        base = floor(sqrt(area))
        # if base ** 2 == area:
        #     return [base]*2

        for i in range(base, 0, -1):
            if area % i == 0:
                return [area//i, i]

        return [area, 1]

# @lc code=end
