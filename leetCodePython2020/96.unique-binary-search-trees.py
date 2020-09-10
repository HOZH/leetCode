#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start

from functools import lru_cache


class Solution:
    def numTrees_rec(self, n: int) -> int:
        @lru_cache(None)
        def helper(start, end):
            if start >= end:
                return 1
            count = 0
            for i in range(start, end+1):
                count += helper(start, i-1)*helper(i+1, end)
            return count
        return helper(1, n)

    def numTrees(self, n: int) -> int:

        dp = [0]*(n+1)
        dp[0] = 1
        # root 1
        # left child j
        # right child i-j-1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]

        return dp[-1]
# @lc code=end
