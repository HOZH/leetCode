#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:

        index = 0
        stack = []
        while index < len(s):
            if s[index] != '*':
                stack.append(s[index])
            else:
                if len(stack) > 0:
                    stack.pop()
            index += 1

        return ''.join(stack)

# @lc code=end
