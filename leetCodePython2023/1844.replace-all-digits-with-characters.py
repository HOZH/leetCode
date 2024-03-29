#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            if i % 2 == 0:
                ans += s[i]
            else:
                ans += chr(ord(s[i-1])+int(s[i]))

        return ans

# @lc code=end
