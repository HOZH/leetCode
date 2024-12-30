#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        steps = 0
        left, right = 0, 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                right += 1
                if left < right:
                    left += 1
                    steps += 1
        return steps + (left-right)


# @lc code=end
