#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
from functools import lru_cache

class Solution:

    def maxCoins(self, nums: List[int]) -> int:

        length = len(nums)

        vals = [1]+nums+[1]

        @lru_cache(None)
        def dp(i, j):

            if i > j:
                return 0

            elif i == j:
                return vals[i-1]*vals[i]*vals[i+1]

            else:

                temp = 0

                for k in range(i, j+1):

                    temp = max(temp, dp(i, k-1) +
                               vals[i-1]*vals[k]*vals[j+1]+dp(k+1, j))

                return temp

        return dp(1, length)

    def maxCoins1(self, nums: List[int]) -> int:
        length = len(nums)

        # initial vals with 1 boundaries on both side
        vals = [1]+nums+[1]

        # dp[a][b] = score for solving sub problem a~b inclusively
        table = [[0]*(length+2) for _ in range(length+2)]

        def dp(i, j):

            if i > j:
                return 0
            # if visited already, return the stored answer
            elif table[i][j]:
                return table[i][j]

            elif i == j:
                return vals[i-1]*vals[i]*vals[i+1]

            else:
                for k in range(i, j+1):
                    # solving dp(i~k-1) and dp(k+1,j) first and save k to the last
                    # which make the reward of taking down
                    # k= i-1 * k * j+1
                    table[i][j] = max(table[i][j], dp(i, k-1) +
                                      vals[i-1]*vals[k]*vals[j+1]
                                      + dp(k+1, j))
                return table[i][j]

        return dp(1, length)


# @lc code=end
