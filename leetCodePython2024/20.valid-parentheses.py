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
