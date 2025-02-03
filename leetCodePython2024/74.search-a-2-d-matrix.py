#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix)-1
        while row_l < row_r:
            row_mid = row_l + (row_r-row_l)//2
            if matrix[row_mid][-1] >= target:
                row_r = row_mid
            else:
                row_l = row_mid+1
        if row_l < 0:
            return False

        l, r = 0, len(matrix[row_l])-1

        while l < r:
            mid = l+(r-l)//2
            if matrix[row_l][mid] >= target:
                r = mid
            else:
                l = mid+1

        return matrix[row_l][l] == target

# @lc code=end
