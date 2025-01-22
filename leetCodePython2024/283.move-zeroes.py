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
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         for j in range(i+1,len(nums)):
        #             if nums[j]!=0:
        #                 nums[i]=nums[j]
        #                 nums[j] = 0
        #                 break
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        # zero_indexes = []
        # other_indexes = []
        # for i in range(len(nums)):
        #     current = nums[i]
        #     if current == 0:
        #         zero_indexes.append(i)
        #     else:
        #         other_indexes.append(i)
        # for j in other_indexes[::-1]:
        #     if len(zero_indexes):
        #         current_index = zero_indexes.pop()
        #         nums[current_index] = nums[j]
        #         nums[j] = 0
                
        #     else:
        #         break



            

        
# @lc code=end

