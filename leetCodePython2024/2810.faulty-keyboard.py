#
# @lc app=leetcode id=2810 lang=python3
#
# [2810] Faulty Keyboard
#

# @lc code=start
class Solution:
    def finalString(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            if s[i] == 'i':
                ans = ans[::-1]
            else:
                ans += s[i]

        return ans

# @lc code=end
