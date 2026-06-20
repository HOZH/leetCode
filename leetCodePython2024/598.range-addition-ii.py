#
# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m*n

        l, w = m, n
        # if ops = [[1,2],[1,2],[2,1]], then result is 1*1 =1
        #  [[1,2],[2,1]]
        for op in ops:
            l = min(l, op[0])
            w = min(w, op[1])

        return l*w


# @lc code=end
