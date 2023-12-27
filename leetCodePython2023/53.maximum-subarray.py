#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf')]*len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1])+nums[i]

        return max(dp)

# @lc code=end
