#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


class Solution:
    def removeDuplicates(self, nums) -> int:

        length = len(nums)
        if length == 0 or length == 1:
            return length

        current, prev, index, count = 0, nums[0], 0, 1

        while index < length-1:

            while nums[index] == prev:

                index += 1

                if index >= length:
                    return count

            current += 1
            nums[current] = nums[index]
            prev = nums[current]
            count += 1

        return count
