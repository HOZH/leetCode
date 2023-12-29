#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        matrix = [[float('inf') for _ in range(len(grid[0])+1)]
                  for _ in range(len(grid)+1)]
        matrix[0][1] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = min(matrix[i-1][j], matrix[i]
                                   [j-1])+grid[i-1][j-1]
        return matrix[-1][-1]

# @lc code=end
