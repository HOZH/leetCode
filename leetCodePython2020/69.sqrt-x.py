#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x+1
        while l < r:
            m = l + (r-l)//2
            temp = m**2
            if temp > x:
                r = m
            else:
                l = m+1
        # round down to the neareset integer
        return l - 1

# @lc code=end
