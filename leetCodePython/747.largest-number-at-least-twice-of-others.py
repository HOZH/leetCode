#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        prev = -1
        current = nums[0]
        index = 0

        for i in range(1, len(nums)):

            if nums[i] > current:
                prev = current
                current = nums[i]
                index = i
            elif nums[i] > prev:
                prev = nums[i]

        if prev == -1:
            return index
        if prev == 0 or current / prev >= 2:
            return index

        return -1
