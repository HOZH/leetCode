#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        sub = ''
        for i in range(n // 2):
            sub += s[i]
            k, r = divmod(n, i + 1)
            if r == 0 and sub * k == s:
                return True

        return False

# @lc code=end
