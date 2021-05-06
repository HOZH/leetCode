#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat, k):
        row, col = len(mat), len(mat[0])
        # b to save sum from (0,0) to (i,j)
        b = [[mat[0][0] for x in range(col)] for y in range(row)]
        # c to save result
        c = [[0 for x in range(col)] for y in range(row)]
        # init b
        for i in range(1, col):
            b[0][i] = b[0][i-1]+mat[0][i]
        for i in range(1, row):
            b[i][0] = b[i-1][0]+mat[i][0]
        # use DP to fill values for b
        for i in range(1, row):
            for j in range(1, col):
                b[i][j] = b[i-1][j]+b[i][j-1]-b[i-1][j-1]+mat[i][j]
                # use dp to fill value for c
        for i in range(0, row):
            for j in range(0, col):
                x1, x2, y1, y2 = i-k-1, i+k, j-k-1, j+k
                if x2 >= row:
                    x2 = row-1
                if y2 >= col:
                    y2 = col-1
                c[i][j] = b[x2][y2]
                if x1 < 0 and y1 >= 0:
                    c[i][j] -= b[x2][y1]
                if x1 >= 0 and y1 < 0:
                    c[i][j] -= b[x1][y2]
                if x1 >= 0 and y1 >= 0:
                    c[i][j] = c[i][j]-b[x2][y1]-b[x1][y2]+b[x1][y1]
                # tricky part is how to judge the boundary
        return c
# @lc code=end
