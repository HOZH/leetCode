#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:

        result = ''
        for i in range(len(s)):
            if ord(s[i]) not in range(48, 58):
                result += s[i]
            else:
                result += chr(ord(s[i-1])+int(s[i]))

        return result
# @lc code=end
