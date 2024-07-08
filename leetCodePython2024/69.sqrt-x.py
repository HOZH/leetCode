#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x+1

        def helper(val):
            return val**2 > x

        while left < right:
            mid = left+(right-left)//2

            if helper(mid):
                right = mid
            else:
                left = mid+1

        return left-1

# @lc code=end
