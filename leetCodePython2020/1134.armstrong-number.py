#
# @lc app=leetcode id=1134 lang=python3
#
# [1134] Armstrong Number
#

# @lc code=start
class Solution:
    def isArmstrong(self, n: int) -> bool:

        power = len(str(n))

        result = 0

        for i in str(n):

            result += int(i)**power

        return n == result


# @lc code=end
