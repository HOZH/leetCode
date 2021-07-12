#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # possible starts all 1s

        # pick a start
        # do dfs and take off all the 1s in that graph
        # count + =1
        # try another remaining start
        # return count after no start point left
        row_len = len(grid)
        if row_len == 0:
            return 0

        col_len = len(grid[0])

        next_move = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(y, x):

            for o, p in next_move:
                new_y, new_x = y+o, x+p
                if 0 <= new_x < col_len and 0 <= new_y < row_len:
                    if grid[new_y][new_x] == '1':
                        grid[new_y][new_x] = '0'
                        dfs(new_y, new_x)

        count = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


# @lc code=end
