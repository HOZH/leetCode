#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start

from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        result = [[0 for _ in range(m+1)] for _ in range(n+1)]
        result[1][1] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j == 1:
                    continue
                result[i][j] = result[i-1][j]+result[i][j-1]

        return result[-1][-1]

    # def uniquePaths_temp(self, m: int, n: int) -> int:

    #     result = [[0 for _ in range(m)] for _ in range(n)]
    #     result[0][0] = 1

    #     queue = deque([(0, 0)])

    #     while len(queue) > 0:

    #         i, j = queue.popleft()

    #         if result[i][j] != 0 and i != 0 and j != 0:
    #             continue

    #         if i > 0:
    #             result[i][j] += result[i - 1][j]

    #         if j > 0:
    #             result[i][j] += result[i][j - 1]

    #         if (i + 1) < n:
    #             queue.append((i + 1, j))

    #         if (j + 1) < m:
    #             queue.append((i, j + 1))

    #     return result[-1][-1]
# @lc code=end
