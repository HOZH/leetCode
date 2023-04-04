#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        for i in s:
            match i:
                case 'L':
                    l += 1
                case 'R':
                    r += 1
            if l == r:
                ans += 1

        return ans

# @lc code=end
