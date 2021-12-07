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
        index, count = 0, 1

        for i in range(1, len(nums)):
            current = nums[i]
            if current != nums[index]:
                index += 1
                count += 1
                nums[index] = current
        return count

# @lc code=end
