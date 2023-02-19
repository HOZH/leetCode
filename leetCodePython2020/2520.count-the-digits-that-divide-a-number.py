#
# @lc app=leetcode id=2520 lang=python3
#
# [2520] Count the Digits That Divide a Number
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:

        count = 0

        for i in str(num):
            if num % int(i) == 0:
                count += 1

        return count

# @lc code=end
