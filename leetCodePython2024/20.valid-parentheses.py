#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s):
            return True
        buffer = []
        temp = {}
        openning = {'(', '[', '{'}


        for i in range(len(s)):
            if len(buffer):
                prev = buffer[-1]
            else:
                prev = None

            current = s[i]

            if current in openning:
                buffer.append(current)
            else:
                match current:
                    case ')':
                        if prev != '(':
                            return False
                    case ']':
                        if prev != '[':
                            return False
                    case '}':
                        if prev != '{':
                            return False
                    case _:
                        pass
                buffer.pop()

        return len(buffer) == 0


# @lc code=end

from collections import deque
from heapq import heapify, heappop, heappush
def isValid(self, s: str) -> bool:
        stack = []
        paran_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        # input  [(, {, [, (, ] ->
        for item in s:
            if item in paran_map:
                # is a closing paran
                if len(stack) < 1: # []
                    # closing paran and empty stack means mismatch
                    return False
                paran_pair = paran_map[item] # (
                top_of_stack = stack[-1] # (
                if paran_pair != top_of_stack:
                    return False
                stack.pop() # []
            else:
                stack.append(item) # [(]
                
        if len(stack) > 0:
            return False
        return True