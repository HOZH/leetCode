#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        indexed_nums = [(value,i) for i,value in enumerate(nums)]
        print(indexed_nums)
        indexed_nums.sort()
        print(indexed_nums)
        result = [-1 for _ in range(len(nums))]

        for new_index in range(len(nums)):
            current = indexed_nums[new_index]
            old_index = current[1]
            result[old_index]= new_index - old_index
        print(result)
        
# @lc code=end

