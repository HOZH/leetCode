#
# @lc app=leetcode id=2520 lang=python3
#
# [2520] Count the Digits That Divide a Number
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        return len(list(filter(lambda y: num % y == 0, list(map(lambda x: int(x), [*str(num)])))))
# @lc code=end
