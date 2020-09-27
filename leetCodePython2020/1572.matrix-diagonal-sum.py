#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        result = 0

        side = len(mat)

        for i in range(side):
            result += mat[i][i]+mat[i][side-i-1]

        if side % 2 == 1:
            result -= mat[side//2][side//2]

        return result

# @lc code=end
