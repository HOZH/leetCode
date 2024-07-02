#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left, right = 0, 0
        ans = 0
        for i in range(len(s)):
            if s[i] == 'L':
                left += 1
            else:
                right += 1
            if left == right:
                ans += 1

        return ans

# @lc code=end
