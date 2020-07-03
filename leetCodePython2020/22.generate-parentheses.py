#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.ans = []

        def helper(left, right, s):

            if left == 0 and right == 0:
                self.ans.append(s)
                return

            # avoiding the cases where string will contain leading '('
            if right < left:
                return

            if left > 0:
                helper(left-1, right, s+'(')

            if right > 0:
                helper(left, right-1, s+')')

        helper(n, n, '')
        return self.ans


# @lc code=end
