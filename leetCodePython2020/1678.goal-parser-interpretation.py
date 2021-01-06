#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:

        result = ''
        i = 0
        while i < len(command):

            current = command[i]

            if current == 'a':
                i += 3
                result += 'al'
                continue

            elif current == 'G':
                result += 'G'

            elif current == ')':
                result += 'o'

            i += 1

        return result


# @lc code=end
