#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#

# @lc code=start
from collections import defaultdict
# 2
# 1,2,0,2,4


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for i in range(len(arr)):
            dp[arr[i]] = dp[arr[i]-difference]+1

        return max(dp.values())

# @lc code=end
