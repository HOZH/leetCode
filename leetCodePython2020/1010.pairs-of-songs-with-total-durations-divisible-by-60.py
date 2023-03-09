#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
from collections import defaultdict
# from math import comb


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        length = len(time)
        bag = defaultdict(int)

        for i in range(length):
            temp = time[i] % 60
            if temp == 0:
                ans += bag[0]
            else:
                ans += bag[60-temp]
            bag[temp] += 1
        return ans

        # dp = [0]*61
        # for i in range(length):
        #     temp = time[i] % 60
        #     ans += dp[60-temp]
        #     dp[temp] += 1

        # return ans+comb(dp[0], 2)

# @lc code=end
