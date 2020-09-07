#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        dp = [i[:] for i in triangle]

        # skip last layer
        for i in range(len(triangle)-2, -1, -1):

            for j in range(len(triangle[i])):

                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])+triangle[i][j]

        return dp[0][0]


# @lc code=end
