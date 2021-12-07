#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = list(filter(lambda x: x != 0, nums))
        temp.extend([0]*(len(nums)-len(temp)))
        for i in range(len(nums)):
            nums[i] = temp[i]

# @lc code=end
