#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        left = right = 0
        ans = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                right += 1

            ans = max(abs(left-right), ans)

        return ans


# @lc code=end
