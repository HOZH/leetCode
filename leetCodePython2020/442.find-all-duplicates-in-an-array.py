#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        rs = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                rs.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return rs
        
# @lc code=end

