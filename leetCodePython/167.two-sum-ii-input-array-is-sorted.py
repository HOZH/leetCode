#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

       


        dic = {}

        for i in range(len(numbers)):
            if target- numbers[i] not in dic:
                dic[numbers[i]]=i
            
            else:
                return [dic[target-numbers[i]]+1,i+1]

            
            

            
        

