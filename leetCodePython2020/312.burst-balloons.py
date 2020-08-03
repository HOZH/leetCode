#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start


class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        length = len(nums)

        # initial vals with 1 boundaries on both side
        vals = [1]+nums+[1]


        # initial a memoization table

        table = [[0]*(length+2) for _ in range(length+2)]

        def dp(i, j):

            if i > j:
                return 0

            if table[i][j] > 0:
                return table[i][j]

            if i == j:
                return vals[i - 1] * vals[i] * vals[i + 1]

            for k in range(i, j+1):
                table[i][j] = max(table[i][j], dp(i, k-1) +
                                  vals[i-1]*vals[k]*vals[j+1]
                                  + dp(k+1, j))

            return table[i][j]

        return dp(1, length)


# @lc code=end
