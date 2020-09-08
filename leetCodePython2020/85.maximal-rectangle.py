#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        row_c = len(matrix)
        if row_c == 0:
            return 0
        col_c = len(matrix[0])

        dp = [[0 for _ in range(col_c)] for _ in range(row_c)]

        for i in range(row_c):
            for j in range(col_c):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = (0 if j == 0 else dp[i][j-1])+1
        ans = 0

        for i in range(row_c):
            for j in range(col_c):
                length = float('inf')

                for k in range(i, row_c):
                    length = min(length, dp[k][j])

                    if length == 0:
                        break
                    ans = max(ans, length*(k-i+1))

        return ans


# @lc code=end
