#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        dp = [1]
        lis = dp
        for i in range(1, rowIndex+1):
            lis = []
            for j in range(i+1):
                if j != 0 and j != i:
                    temp = dp[j-1] + dp[j]
                else:
                    temp = 1
                lis.append(temp)
            dp = lis
        return dp
# @lc code=end
