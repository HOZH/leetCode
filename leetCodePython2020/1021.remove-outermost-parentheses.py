#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        l, r = 0, 0
        temp = []
        for i in range(len(S)):
            current = S[i]
            if current == '(':
                l += 1
                temp.append('(')
            else:
                r += 1
                temp.append(')')
                if l == r:
                    result.extend(temp[1:-1])
                    temp = []
                    l, r = 0, 0
        return ''.join(result)


# @lc code=end
