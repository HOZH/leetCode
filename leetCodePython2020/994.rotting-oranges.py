#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        col_len, row_len = len(grid), len(grid[0])
        temp_grid = []
        for i in grid:
            temp_grid.append(i[::])

        def helper(m, n):
            next_locations = ((-1, 0), (1, 0), (0, 1), (0, -1))
            rot_others = False
            for i, j in next_locations:
                if 0 <= m + i < col_len and 0 <= n + j < row_len:
                    if grid[m + i][n + j] == 1:
                        temp_grid[m + i][n + j] = 2
                        rot_others = True
            return rot_others

        ans = 0
        while True:
            flag = False
            for i in range(col_len):
                for j in range(row_len):
                    if grid[i][j] == 2:
                        flag = helper(i, j) or flag
                        grid[i][j] = 3
            for i in range(col_len):
                grid[i] = temp_grid[i][::]
            prev_ans = ans
            if flag:
                ans += 1

            if ans == prev_ans:
                for i in range(col_len):
                    for j in range(row_len):
                        if grid[i][j] == 1:
                            return -1
                return ans


# @lc code=end
