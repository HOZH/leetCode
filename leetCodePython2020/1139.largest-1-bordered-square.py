#
# @lc app=leetcode id=1139 lang=python3
#
# [1139] Largest 1-Bordered Square
#

# @lc code=start


class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        # print(grid)
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        row_len, col_len = len(grid), len(grid[0])
        table = [[0 for _ in range(col_len)] for _ in range(row_len)]
        for i in range(row_len):
            table[i][-1] = 0 if grid[i][-1] == 0 else 1

            for j in range(col_len - 2, -1, -1):
                table[i][j] = 0 if grid[i][j] == 0 else table[i][j + 1] + 1

        result_side = 0
        for i in grid:
            if 1 in i:
                result_side = 1
                break
        # max_side = min(row_len, col_len)

        for i in range(row_len):

            for j in range(col_len):

                temp_side = table[i][j]
                if temp_side > result_side:

                    skip_current = False

                    for k in range(temp_side - 1, 0, -1):

                        if skip_current:
                            break

                        if i + k >= len(table):
                            pass

                        elif table[i + k][j] >= k + 1:
                            h_flag = True
                            for l in range(i + 1, i + k):
                                if table[l][j] == 0 or table[l][j + k] == 0:
                                    h_flag = False
                                    break
                            if not h_flag:
                                pass
                            else:
                                if (k + 1) > result_side:
                                    result_side = k + 1
                                skip_current = True

                        else:
                            pass

                else:
                    pass
        # print(result_side)
        # print(table)
        pass
        return result_side ** 2

# @lc code=end
