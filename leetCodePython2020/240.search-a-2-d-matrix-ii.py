#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# @lc code=start


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not len(matrix) or not len(matrix[0]):
            return False

        m, n = len(matrix), len(matrix[0])

        r, c = 0, n-1

        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True

            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1

        return False

# @lc code=end
