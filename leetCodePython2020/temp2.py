class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def bk(s, left, right):
            if len(s) == 2*N:
                ans.append(s)
                return
            if left<N:
                bk(s+'(', left+1, right) # called N times"""
            if right<left:
                bk(s+')', left, right+1) # 
        bk('', 0, 0)
        return ans


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.ans = []

        def helper(left, right, s):

            if left == 0 == right:

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

