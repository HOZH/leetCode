#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:


        
        #coulda been much faster if I check dup eles by looping through each individually
        #with addition lines tho
        return True if len(set(nums)) != len(nums) else False


        

