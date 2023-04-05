#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        current = 0
        for i in s:
            if i == '(':
                current += 1
            elif i == ')':
                ans = max(ans, current)
                current -= 1

        return max(ans, current)

# @lc code=end
