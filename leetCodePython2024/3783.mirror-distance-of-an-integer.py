#
# @lc app=leetcode id=3783 lang=python3
#
# [3783] Mirror Distance of an Integer
#

# @lc code=start
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n-int(str(n)[::-1]))

# @lc code=end
