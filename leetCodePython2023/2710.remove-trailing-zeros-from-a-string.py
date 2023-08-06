#
# @lc app=leetcode id=2710 lang=python3
#
# [2710] Remove Trailing Zeros From a String
#

# @lc code=start
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while len(num) > 0 and num[-1] == '0':
            num = num[:-1]
        return num

# @lc code=end
