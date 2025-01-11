#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        prev = nums[0]
        next_insertion_index = 1

        for i in range(1, len(nums)):
            current = nums[i]
            if current == prev:
                continue
            else:
                prev = current
                nums[next_insertion_index] = current
                next_insertion_index += 1

        return next_insertion_index


# @lc code=end
