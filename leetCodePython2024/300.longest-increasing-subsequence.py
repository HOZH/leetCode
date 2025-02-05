#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(dp)):
            local_result = dp[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    local_result = max(dp[j]+1, local_result)
            dp[i] = local_result
        return max(dp)

# @lc code=end
