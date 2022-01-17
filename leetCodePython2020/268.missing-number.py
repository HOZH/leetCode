#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        return int(length*(length+1)/2-sum(nums))

# @lc code=end
