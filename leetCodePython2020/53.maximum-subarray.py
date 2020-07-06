#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result = [0]*len(nums)
        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = max(result[i-1]+nums[i], nums[i])

        return max(result)


# @lc code=end
