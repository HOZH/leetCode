#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        result = [[0 for _ in range(m+1)] for _ in range(n+1)]
        # result[1][1] = 1
        for i in range(n+1):
            result[i][0] = -1
        for i in range(m+1):
            result[0][i] = -1
        for i in range(1, n+1):
            for j in range(1, m+1):
                mapped_val = grid[i-1][j-1]
                result[i][j] = mapped_val

        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j == 1:
                    continue
                a, b = result[i-1][j], result[i][j-1]
                if a == -1:
                    result[i][j] += b
                elif b == -1:
                    result[i][j] += a
                else:
                    result[i][j] += min(a, b)

        return result[-1][-1]

# @lc code=end
