#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start

from collections import deque


class Solution:
    def updateMatrix(self, matrix):

        result = [[-1 for j in range(len(matrix[0]))]
                  for i in range(len(matrix))]

        starts, ones = [], []

        # get zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:
                    result[i][j] = 0
        # get ones
        for a in range(len(result)):
            for b in range(len(result[0])):

                if result[a][b] == 0:
                    positions = [(a - 1, b), (a + 1, b),
                                 (a, b - 1), (a, b + 1)]

                    for c in positions:
                        y, x = c
                        if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
                            if result[y][x] != 0:
                                result[y][x] = 1
                                ones.append([y, x])

        def bfs(arr):

            while len(arr) > 0:
                ny, nx = arr.popleft()
                positions = [(ny - 1, nx), (ny + 1, nx),
                             (ny, nx - 1), (ny, nx + 1)]
                for k in positions:
                    y, x = k
                    if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):

                        if result[y][x] == -1:
                            result[y][x] = result[ny][nx] + 1

                            arr.append((y, x))

                        elif result[y][x] < 3:
                            pass
                        else:
                            temp = result[ny][nx] + 1
                            if temp < result[y][x]:
                                result[y][x] = temp
                                arr.append((y, x))

        for k in ones:
            i, j = k
            bfs(deque([(i, j)]))
        return result


# @lc code=end
