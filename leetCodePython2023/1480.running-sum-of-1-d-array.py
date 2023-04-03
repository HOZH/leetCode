#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if not length:
            return []
        ans = [0]*length
        ans[0] = nums[0]
        for i in range(1, length):
            ans[i] = ans[i-1]+nums[i]
        
        return ans
# @lc code=end
