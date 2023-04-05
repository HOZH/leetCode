#
# @lc app=leetcode id=2500 lang=python3
#
# [2500] Delete Greatest Value in Each Row
#

# @lc code=start
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort()

        ans = 0

        for i in range(len(grid[0])):
            current_max = 0
            for j in range(len(grid)):
                current_max = max(grid[j][i], current_max)
            ans += current_max

        return ans


# @lc code=end
