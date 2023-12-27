#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])

        return dp[-1]


# @lc code=end
