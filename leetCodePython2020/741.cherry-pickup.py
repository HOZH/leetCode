#
# @lc app=leetcode id=741 lang=python3
#
# [741] Cherry Pickup
#

# @lc code=start


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        n = len(grid)
        memo = [[[-2 for _ in range(n)] for _ in range(n)] for _ in range(n)]

        def dp(x1, x2, y1):

            y2 = x1+y1-x2

            if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
                return -1

            if grid[y1][x1] < 0 or grid[y2][x2] < 0:
                return -1

            # can either be 1 or 0
            if x1 == 0 and y1 == 0:
                return grid[y1][x1]

            if memo[x1][x2][y1] >= -1:
                return memo[x1][x2][y1]

            ans = max(dp(x1-1, x2-1, y1), dp(x1, x2, y1-1),
                      dp(x1, x2-1, y1-1), dp(x1-1, x2, y1))

            if ans < 0:
                memo[x1][x2][y1] = -1
                return -1

            ans += grid[y1][x1]
            if x1 != x2:
                ans += grid[y2][x2]

            memo[x1][x2][y1] = ans

            return ans

        return max(0, dp(n-1, n-1, n-1))


# @lc code=end
