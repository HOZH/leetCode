#
# @lc app=leetcode id=2119 lang=python3
#
# [2119] A Number After a Double Reversal
#

# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0

# @lc code=end
