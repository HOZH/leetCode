#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start


class Solution:
    def balancedStringSplit(self, s: str) -> int:

        # it's gurrantted input as a balanced string

        count = 0
        l, r = 0, 0
        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            else:
                r += 1
            if l == r and l != 0:
                count += 1
                l, r = 0, 0
        return count

        # @lc code=end
