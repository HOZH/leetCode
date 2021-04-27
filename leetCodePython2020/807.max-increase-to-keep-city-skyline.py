#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#

# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        row_maxes, col_maxes = [0]*len(grid), [0]*len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row_maxes[i] = max(row_maxes[i], grid[i][j])
                col_maxes[j] = max(col_maxes[j], grid[i][j])

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(row_maxes[i], col_maxes[j])-grid[i][j]

        return ans


# @lc code=end
