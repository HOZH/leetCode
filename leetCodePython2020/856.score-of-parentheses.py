#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        def helper(index):
            current_score = 0
            while index < len(S):
                if S[index] == '(':
                    temp = helper(index + 1)
                    index = temp[0]
                    current_score += temp[1]
                else:
                    return index + 1, 1 if current_score == 0 else 2 * current_score

            return index + 1, current_score

        return helper(0)[1]
        
# @lc code=end

