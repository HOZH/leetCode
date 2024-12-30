#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from collections import defaultdict


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # layers = defaultdict(list)
        # n = len(matrix)
        # for i in range(0, n):
        #     for col in range(i, n - i):
        #         layers[i].append((matrix[i][col], i, col))
        #     for row in range(i + 1, n - i - 1):
        #         layers[i].append((matrix[row][-i - 1], row, -i - 1))
        #     if i != n - i - 1:
        #         for col in range(n - i - 1, i - 1, -1):
        #             layers[i].append((matrix[-i - 1][col], -i - 1, col))
        #     for row in range(n - i - 1 - 1, i, -1):
        #         layers[i].append((matrix[row][i], row, i))

        # for layer in layers.keys():
        #     ele_in_current_layer = layers[layer]
        #     step = n - 1 - layer * 2
        #     if step != 0:
        #         for initial_index in range(step):
        #             current = ele_in_current_layer[initial_index]
        #             index = initial_index
        #             initial = ele_in_current_layer[initial_index]
        #             while current:
        #                 index += step
        #                 if index < len(ele_in_current_layer):
        #                     next_ele = ele_in_current_layer[index]
        #                     matrix[next_ele[1]][next_ele[2]] = current[0]
        #                     current = next_ele
        #                 else:
        #                     break

        #             matrix[initial[1]][initial[2]] = next_ele[0]

        # n = len(matrix[0])
        # for i in range(n // 2 + n % 2):
        #     for j in range(n // 2):
        #         tmp = matrix[n - 1 - j][i]
        #         matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
        #         matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
        #         matrix[j][n - 1 - i] = matrix[i][j]
        #         matrix[i][j] = tmp

        n = len(matrix[0])
        left, right = 0, n-1

        while left < right:
            for i in range(right-left):
                top = left
                bottom = right
                temp = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = temp
            left += 1
            right -= 1


# @lc code=end
