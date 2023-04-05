#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        temp = [[0]*length for i in range(length)]
        for i in range(length):
            for j in range(length):
                if 0 < i < len(grid)-1 and 0 < j < len(grid)-1:
                    temp[i][j] = max(grid[i][j], grid[i-1][j],
                                     grid[i][j-1], grid[i+1][j], grid[i][j+1], grid[i-1][j-1], grid[i+1][j+1], grid[i-1][j+1], grid[i+1][j-1])

        temp = temp[1:-1]
        for i in range(len(temp)):
            temp[i] = temp[i][1:-1]

        return temp


# @lc code=end
