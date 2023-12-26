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

        ones = []

        # get zeros
        # get ones
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:
                    result[i][j] = 0
                    positions = [(i - 1, j), (i + 1, j),
                                 (i, j - 1), (i, j + 1)]
                    for c in positions:
                        y, x = c
                        if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
                            if matrix[y][x] != 0:
                                result[y][x] = 1
                                ones.append([y, x])

        def bfs(stack):
            while len(stack) > 0:
                y, x = stack.popleft()
                positions = [(y - 1, x), (y + 1, x),
                             (y, x - 1), (y, x + 1)]
                for k in positions:
                    ny, nx = k
                    if 0 <= ny < len(matrix) and 0 <= nx < len(matrix[0]):

                        if result[ny][nx] == -1:
                            result[ny][nx] = result[y][x] + 1
                            stack.append((ny, nx))
                        # case 0,1 is already determined, case 2 will
                        # become the new base case (can't has smaller number, if it's 0 or 1 should already be modified)
                        # so it's ignored also
                        elif result[ny][nx] < 3:
                            pass
                        else:
                            temp = result[y][x] + 1
                            if temp < result[ny][nx]:
                                result[ny][nx] = temp
                                stack.append((ny, nx))

        for k in ones:
            i, j = k
            bfs(deque([(i, j)]))
        return result


# @lc code=end
