#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # len_nums=len(nums)
        # dic=dict()
        # for i in range(len_nums):

        #     if i+1 < len_nums:

        #         try:
        #             complement = nums[i+1:].index(target-nums[i])

        #         except ValueError:
        #             continue

        #         return [i, complement+i+1]

        #     else:
        #         break

        dic = {}
        for i in range(len(nums)):
            if target-nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return [dic[target-nums[i]], i]
        


        

        
