#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        
        for i in range(len(nums)):
            if nums[i] not in table:
                table[target-nums[i]]=i
            else:
                return [i,table[nums[i]]]
        
        
# @lc code=end
