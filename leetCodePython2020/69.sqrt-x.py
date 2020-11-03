#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x

        while l <= r:

            pivot = l+(r-l)//2

            temp = pivot**2
            if temp == x:
                # if temp == x or (temp < x and (pivot+1)**2 > x):
                return pivot

            elif temp > x:
                r = pivot-1

            else:
                if (pivot+1)**2 > x:
                    return pivot
                l = pivot+1


# @lc code=end
