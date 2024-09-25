#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [float('-inf')]*len(nums)
        for i in range(len(nums)):
            ans[i]=nums[nums[i]]
        
        return ans
        
# @lc code=end

