#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start

class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        ans = [[float('inf') for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if i > 0:
                        ans[i][j] = min(ans[i][j], ans[i-1][j]+1)
                    if j > 0:
                        ans[i][j] = min(ans[i][j], ans[i][j-1]+1)
                else:
                    ans[i][j] = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j]:
                    if i < m-1:
                        ans[i][j] = min(ans[i][j], ans[i+1][j]+1)
                    if j < n-1:
                        ans[i][j] = min(ans[i][j], ans[i][j+1]+1)
        return ans

        
# @lc code=end

