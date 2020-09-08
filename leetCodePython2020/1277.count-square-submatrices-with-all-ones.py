#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#

# @lc code=start


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        ans = 0
        # max length of square edge
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = matrix[i][j]

                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
                ans += dp[i][j]

        return ans

# @lc code=end
