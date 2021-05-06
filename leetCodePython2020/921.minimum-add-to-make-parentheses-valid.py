#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
from collections import deque


class Solution:
    def minAddToMakeValid(self, S: str) -> int:

        if not S:
            return 0

        stack = deque(S[0])

        for i in S[1:]:

            if i == ')':
                if stack and stack[0] == '(':
                    stack.popleft()
                    continue

            stack.appendleft(i)

        return len(stack)


# @lc code=end
