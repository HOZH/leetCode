#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:

    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)
        vals = tuple([1]+nums+[1])

        @lru_cache(None)
        def dp(i, j):

            if i > j:
                return 0

            elif i == j:
                return vals[i-1]*vals[i]*vals[i+1]
            else:
                temp = 0
                for k in range(i, j+1):
                    # solving dp(i,k-1) and dp(k+1,j) first and save k to the last
                    # which make the reward of taking down
                    # k= i-1 * k * j+1
                    temp = max(temp, dp(i, k-1) +
                               vals[i-1]*vals[k]*vals[j+1]+dp(k+1, j))

                return temp

        return dp(1, n)

# @lc code=end
