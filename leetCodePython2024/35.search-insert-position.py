#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left

# @lc code=end
