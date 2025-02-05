#
# @lc app=leetcode id=1139 lang=python3
#
# [1139] Largest 1-Bordered Square
#

# @lc code=start
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            prev = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dp[i][j] = prev+1
                    prev += 1
                else:
                    prev = 0
        max_side = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                upside_width = dp[i][j]
                # if upside_width !=0:
                if upside_width > max_side:
                    # for k in range(upside_width,0,-1):
                    for k in range(upside_width, max_side, -1):
                        if (i+k-1) < len(grid) and dp[i+k-1][j] >= k:
                            board_exists = True
                            for l in range(i+1, i+k-1):
                                if grid[l][j-k+1] == 1 and grid[l][j] == 1:
                                    continue
                                else:
                                    board_exists = False
                                    break
                            if board_exists:
                                max_side = max(max_side, k)

        return max_side**2

# @lc code=end
