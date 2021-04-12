#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return S
        res = [S[0]]
        for curr in S[1:]:
            if res and curr == res[-1]:
                res.pop()
            else:
                res.append(curr)
        res = ''.join(res)
        return res
# @lc code=end
