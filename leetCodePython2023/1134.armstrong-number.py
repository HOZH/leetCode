#
# @lc app=leetcode id=1134 lang=python3
#
# [1134] Armstrong Number
#

# @lc code=start
class Solution:
    def isArmstrong(self, n: int) -> bool:
        temp = str(n)
        result = 0
        power = len(temp)
        for i in temp:
            result += int(i)**power
        return result == n

# @lc code=end
