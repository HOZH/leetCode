#
# @lc app=leetcode id=1180 lang=python3
#
# [1180] Count Substrings with Only One Distinct Letter
#

# @lc code=start
class Solution:
    def countLetters(self, s: str) -> int:

        total = 1
        sub = [0]*len(s)
        sub[0] = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                sub[i] = sub[i-1]+1
            else:
                sub[i] = 1
            total += sub[i]

        return total

# @lc code=end
