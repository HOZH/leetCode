#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        total, y, x = 0, len(grid), len(grid[0])

        for current_y in range(y):
            current_x = 0

            while current_x < x:

                if grid[current_y][current_x] < 0:
                    temp = (x-current_x)*(y-current_y)
                    total += temp
                    x = current_x
                    break

                current_x += 1

        return total

# @lc code=end
