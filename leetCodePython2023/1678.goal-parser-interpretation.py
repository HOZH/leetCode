#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        ans = ''
        for i in command:
            match i:
                case ')':
                    if stack[-1] == 'l':
                        ans += 'al'
                        stack = stack[:-3]
                    else:
                        ans += 'o'
                        stack = stack[:-1]
                case 'G':
                    ans += 'G'
                    stack = stack[:-1]
                case _:
                    stack.append(i)

        return ans

        # for i in command:
        #     if i == ')':
        #         if stack[-1] == 'l':
        #             ans += 'al'
        #             stack = stack[:-3]
        #         else:
        #             ans += 'o'
        #             stack = stack[:-1]
        #     elif i == 'G':
        #         ans += 'G'
        #     else:
        #         stack.append(i)

        # return ans


# @lc code=end
