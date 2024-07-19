#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = current = ''
        left, right = 0, 0
        for i in range(len(s)):
            current_char = s[i]
            if current_char == '(':
                left += 1
            elif current_char == ')':
                right += 1

            current += current_char
            if left == right:
                ans += current[1:-1]
                current = ''

        return ans


# @lc code=end
