#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairs = {')': '(', '}': '{', ']': '['}
        tails = set(')}]')

        for i in range(len(s)):
            if s[i] in tails:
                if not len(stack):
                    return False
                if pairs[s[i]] == stack[-1]:
                    stack.pop()
                    continue

            stack.append(s[i])

        return len(stack) == 0


# @lc code=end
