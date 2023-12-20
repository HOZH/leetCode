#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix)
        while l < r:
            m = l+(r-l)//2
            if matrix[m][0] == target:
                return True
            
            if matrix[m][0] > target:
                r = m
            else:
                l = m+1

        row = l-1

        l, r = 0, len(matrix[0])
        while l < r:
            m = l+(r-l)//2
            if matrix[row][m] == target:
                return True

            if matrix[row][m] > target:
                r = m
            else:
                l = m+1

        return matrix[row][l-1] == target


# @lc code=end
