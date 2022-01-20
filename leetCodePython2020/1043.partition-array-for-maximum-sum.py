#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]*(len(arr)+1)
        for i in range(1, len(arr)+1):
            for j in range(1, k+1):
                if i < j:
                    break
                # dp is 1 indexed
                dp[i] = max(dp[i], dp[i-j]+max(arr[i-j:i])*j)
        return dp[-1]


# @lc code=end
