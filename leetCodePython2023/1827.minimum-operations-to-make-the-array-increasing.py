#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        prev = nums[0]

        result = 0
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                lacked_val = prev-nums[i]+1
                result += lacked_val
                prev = nums[i]+lacked_val
            else:
                prev = nums[i]

        return result


# @lc code=end
