#
# @lc app=leetcode id=2482 lang=python3
#
# [2482] Difference Between Ones and Zeros in Row and Column
#

# @lc code=start
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        ones_row, zeros_row = [],[]
        ones_col, zeros_col = [],[]
        for i in range(m):
            ones = 0
            for j in range(n):
                ones+=grid[i][j] 
                
            ones_row.append(ones)
            zeros_row.append(n-ones)

        for i in range(n):
            ones = 0
            for j in range(m):
                ones+=grid[j][i] 
                
            ones_col.append(ones)
            zeros_col.append(m-ones)
        
        diffs = [ [ 0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diffs[i][j] = ones_row[i]+ones_col[j]-zeros_row[i]-zeros_col[j]

        
        return diffs
        

        
# @lc code=end

