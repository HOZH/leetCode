#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        if not len(nums):
            return 0

        total = sum(nums)

        # case 1, regular
        dp1 = [0 for _ in range(len(nums))]
        dp1[0] = nums[0]
        for i in range(1, len(nums)):
            dp1[i] = nums[i] + max(dp1[i - 1], 0)

        case1 = max(dp1)

        # case 2, maximun subarray is connected at both the end and the begining of the array

        dp2 = [float('inf') for _ in range(len(nums))]
        dp2[0] = nums[0]
        for i in range(1, len(nums)):
            dp2[i] = nums[i] + min(dp2[i - 1], 0)

        case2 = min(dp2)

        return max(nums) if all(list(map(lambda x: True if x <= 0 else False, nums)))else max(total - case2, case1)

# @lc code=end
