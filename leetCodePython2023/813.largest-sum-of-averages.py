#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#

# @lc code=start
from functools import lru_cache


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:

        @lru_cache(None)
        def get_avg_inclusive(start, end):
            return sum(nums[start:end+1])/(end-start+1)

        dp = [[0 for _ in range(k+1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][1] = get_avg_inclusive(0, i)

        for i in range(len(nums)):
            for j in range(2, k+1):
                for l in range(i-1, -1, -1):
                    dp[i][j] = max(dp[i][j], dp[l][j-1] +
                                   get_avg_inclusive(l+1, i))

        return dp[-1][-1]

# @lc code=end
