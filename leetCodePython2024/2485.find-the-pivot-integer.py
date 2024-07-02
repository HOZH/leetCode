#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        current = 0
        total = sum([i for i in range(0, n+1)])
        print(total)
        for i in range(1, n+1):
            if current == (total-i)/2:
                return i
            current += i

        return -1

# @lc code=end
