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
            m = l+(r-l)//2
            #  minimal k satisfying condition k^2 > x, then k - 1 is the answer to the question.
            if m**2 > x:
                r = m
            else:
                l = m+1

        return l-1

# @lc code=end
