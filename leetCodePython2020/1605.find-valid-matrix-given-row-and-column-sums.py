#
# @lc app=leetcode id=1605 lang=python3
#
# [1605] Find Valid Matrix Given Row and Column Sums
#

# @lc code=start
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        ans = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]

        i, j = 0, 0
        while i < len(rowSum) and j < len(colSum):

            ans[i][j] = min(colSum[j], rowSum[i])

            colSum[j] -= ans[i][j]
            rowSum[i] -= ans[i][j]

            if colSum[j] == 0:
                j += 1
            if rowSum[i] == 0:
                i += 1

        return ans


# @lc code=end
