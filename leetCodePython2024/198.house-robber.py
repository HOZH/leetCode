#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]

# @lc code=end
