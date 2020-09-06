#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        if n == 0:
            return 0
        m = len(obstacleGrid[0])
        result = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                mapped_val = obstacleGrid[i-1][j-1]
                result[i][j] = mapped_val if mapped_val != 1 else -1

        result[1][1] = 1 if result[1][1] == 0 else -1
        if result[1][1] == -1:
            return 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j == 1:
                    continue
                if result[i][j] == -1:
                    continue
                a, b = result[i-1][j], result[i][j-1]
                result[i][j] = (0 if a == -1 else a)+(0 if b == -1 else b)

        return max(result[-1][-1], 0)

# @lc code=end
