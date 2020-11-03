#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start


class Solution:
    # def searchInsert_temp(self, nums: List[int], target: int) -> int:

    #     if len(nums) == 1:
    #         return 0 if target <= nums[0] else 1

    #     result = 0

    #     while len(nums) > 1:
    #         pivot = len(nums)//2
    #         if target == nums[pivot]:
    #             result += pivot
    #             break

    #         left, right = nums[:pivot], nums[pivot:]
    #         # if target == nums[pivot]:
    #         #     result += pivot
    #         #     break
    #         # el
    #         if target <= left[-1]:
    #             nums = left

    #         elif target >= right[0]:
    #             nums = right
    #             result += pivot

    #             if len(right) == 1:
    #                 result += 1

    #         else:
    #             result += pivot
    #             break
    #     return result
    def searchInsert(self, nums, target: int) -> int:
        length = len(nums)
        if length == 1:
            return 0 if target <= nums[0] else 1

        l, r = 0, length-1
        while l <= r:
            pivot = l + (r - l) // 2

            if target == nums[pivot]:
                return pivot

            if nums[pivot] > target:
                r = pivot - 1

            # elif target >= nums[pivot]:
            else:
                l = pivot + 1

            # else:
            #     return pivot
        return l
        # @lc code=end
