#
# @lc app=leetcode id=3173 lang=python3
#
# [3173] Bitwise OR of Adjacent Elements
#

# @lc code=start
class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)-1):
            ans.append(nums[i]|nums[i+1])
        return ans
        
# @lc code=end

