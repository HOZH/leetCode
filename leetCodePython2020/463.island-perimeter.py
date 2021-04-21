#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        row_len, col_len = len(grid), len(grid[0])
        ans = 0

        for i in range(row_len):

            for j in range(col_len):

                if grid[i][j] == 1:

                    for y_offset, x_offset in moves:
                        if not 0 <= (y_offset+i) < row_len or not 0 <= (x_offset+j) < col_len:
                            ans += 1
                        else:
                            ans += 0 if (grid[y_offset +
                                              i][x_offset+j]) == 1 else 1

        return ans


# @lc code=end
