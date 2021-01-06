#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start

from functools import lru_cache


class Solution:

    # def tribonacci(self, n: int) -> int:

    #     dp = [0]*(max(n, 3)+1)
    #     dp[1], dp[2], dp[3] = 1, 1, 2

    #     for i in range(4, n+1):
    #         dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    #     return dp[n]

    @lru_cache(None)
    def tribonacci(self, n: int) -> int:

        if n < 4:
            if not n:
                return 0
            elif n < 3:
                return 1
            else:
                return 2

        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)


# @lc code=end
