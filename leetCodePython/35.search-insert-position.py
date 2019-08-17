#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


class Solution:
    def searchInsert(self, nums, target: int) -> int:

        length = len(nums)
        if length == 0:
            return 0

        if length == 1:
            return 0 if target <= nums[0] else 1
        left = 0
        right = length - 1
        pivot = (right + left)//2
        prev = 0
        target_is_smaller = True

        while left <= right:

            current = nums[pivot]
            if current == target:

                return pivot

            elif current < target:

                target_is_smaller = False

                left = pivot + 1

            else:

                target_is_smaller = True

                right = pivot - 1

            prev = pivot
            pivot = (left + right) // 2

        return prev if target_is_smaller else prev+1
