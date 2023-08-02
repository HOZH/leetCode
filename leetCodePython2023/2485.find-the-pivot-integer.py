#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        current = 0
        target = (1+n)*n//2
        for i in range(1, n+1):
            if current == (target-i)/2:
                return i
            current += i

        return -1

# @lc code=end
