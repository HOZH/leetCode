#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:

        length = len(nums)
        if not length:
            return 0

        # dp[i]->max profit can get til i's
        dp = [0]*length
        dp[0] = nums[0]
        if length > 1:
            dp[1] = max(nums[1], dp[0])

        for i in range(2, length):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]


# @lc code=end
