#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
from collections import deque


class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []
        for ch in s:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        return ''.join(output)

        # def helper(current):
        #     if len(set([*current])) == 1:
        #         return current[0]

        #     stack = deque([])
        #     prev = None
        #     for i in range(len(current)):
        #         if current[i] != prev:
        #             encountered_dup = False
        #         else:
        #             encountered_dup = True

        #         prev = current[i]
        #         stack.append(current[i])
        #         if encountered_dup:
        #             dup_ele = stack[-1]
        #             while len(stack) and stack[-1] == dup_ele:
        #                 stack.pop()
        #             stack.extend([*current[i+1:]])

        #             return helper(''.join(stack))

        #     return ''.join(stack)

        # return helper(s)


# @lc code=end
