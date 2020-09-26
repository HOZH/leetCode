#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        if not len(nums):
            return []

        sums = [0]*len(nums)
        sums[0] = nums[0]

        for i in range(1, len(nums)):
            sums[i] = sums[i-1]+nums[i]

        return sums


# @lc code=end
