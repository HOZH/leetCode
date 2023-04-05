#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        ans = ''
        for i in s:
            if i == '(':
                if depth != 0:
                    ans += i
                depth += 1
            elif i == ')':
                depth -= 1
                if depth != 0:
                    ans += i

        return ans


# @lc code=end
