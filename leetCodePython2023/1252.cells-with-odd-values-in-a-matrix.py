#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0]*n for _ in range(m)]
        for r, c in indices:
            for i in range(n):
                matrix[r][i] += 1
            for j in range(m):
                matrix[j][c] += 1

        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 != 0:
                    result += 1

        return result

# @lc code=end
