#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.ans = []

        def helper(remaining_left, remaining_right, current):
            if remaining_left < 0 or remaining_right < 0:
                return

            if remaining_left == remaining_right == 0:
                self.ans.append(current)
                return

            if remaining_left == remaining_right:
                helper(remaining_left-1, remaining_right, current+'(')
            elif remaining_left < remaining_right:
                helper(remaining_left-1, remaining_right, current+'(')
                helper(remaining_left, remaining_right-1, current+')')
            elif remaining_left > remaining_right:
                return

        helper(n, n, '')
        return self.ans


# @lc code=end
