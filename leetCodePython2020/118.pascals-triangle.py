#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        dp = [[1]]
        for i in range(1, numRows):
            lis = []
            for j in range(i+1):
                if j != 0 and j != i:
                    temp = dp[i-1][j-1] + dp[i-1][j]
                else:
                    temp = 1
                lis.append(temp)
            dp.append(lis)

        return dp


# @lc code=end
