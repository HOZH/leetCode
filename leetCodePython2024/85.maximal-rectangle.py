#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    if j >= 1:
                        dp[i][j] = dp[i][j-1]+1
                    else:
                        dp[i][j] = 1

        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])-1, -1, -1):
                if dp[i][j] != 0:
                    if i > 0 and dp[i-1][j] >= dp[i][j]:
                        continue
                width = dp[i][j]
                height = 1
                max_area = max(max_area, width*height)
                for k in range(i+1, len(matrix)):
                    current_width = dp[k][j]
                    if current_width == 0:
                        break
                    else:
                        width = min(width, current_width)
                        height += 1
                        max_area = max(max_area, width*height)

        return max_area
        
# @lc code=end

