#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:

        if not len(A):
            return 0
        row_len, col_len = len(A), len(A[0])

        dp = [[0]*col_len for _ in range(row_len)]
        dp[0] = A[0][:]

        for i in range(1, row_len):
            for j in range(col_len):
                dp[i][j] = A[i][j]+min(dp[i-1][j], float('inf') if j-1 < 0 else dp[i-1]
                                       [j-1], float('inf') if j+1 >= col_len else dp[i-1][j+1])

        return min(dp[-1])

# @lc code=end
