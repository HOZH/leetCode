#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from math import sqrt, floor


class Solution:
    def numSquares(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # square_nums = [1]
        # dp = [0]*(n+1)
        # dp[1] = 1
        # for i in range(2, len(dp)):
        #     if floor(sqrt(i))**2 == i:
        #         square_nums.append(i)
        #         dp[i] = 1
        #         continue
        #     local_result = float('inf')
        #     for j in range(len(square_nums)-1, -1, -1):
        #         local_result = min(local_result, 1+dp[i-square_nums[j]])
        #     dp[i] = local_result
        # return dp[-1]
        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = min([dp[i-j*j] for j in range(1, int(pow(i, 0.5))+1)]) + 1
        return dp[-1]



# @lc code=end
