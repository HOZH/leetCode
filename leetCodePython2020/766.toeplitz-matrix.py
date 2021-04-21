#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for i in range(len(matrix[0])):

            value = matrix[0][i]
            next_col = i+1

            for j in range(1, len(matrix)):

                if next_col < len(matrix[0]):

                    if matrix[j][next_col] != value:

                        return False
                    else:
                        next_col += 1

                else:
                    break

        for i in range(1, len(matrix)):
            value = matrix[i][0]
            next_col = 1

            for j in range(i+1, len(matrix)):

                if next_col < len(matrix[0]):

                    if matrix[j][next_col] != value:

                        return False
                    else:
                        next_col += 1

                else:
                    break

        return True

# @lc code=end
