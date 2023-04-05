#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        length = len(mat)
        current_row, current_col = 0, 0

        while current_row < length:
            ans += mat[current_row][current_col]
            current_row += 1
            current_col += 1

        current_row, current_col = len(mat)-1, 0
        while current_row > -1:
            ans += mat[current_row][current_col]
            print(mat[current_row][current_col])
            current_row -= 1
            current_col += 1

        return ans - (0 if length % 2 == 0 else mat[length//2][length//2])

# @lc code=end
