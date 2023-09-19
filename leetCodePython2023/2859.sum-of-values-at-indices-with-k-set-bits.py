#
# @lc app=leetcode id=2859 lang=python3
#
# [2859] Sum of Values at Indices With K Set Bits
#

# @lc code=start
class Solution():
    def sumIndicesWithKSetBits(self, nums, k):
        result = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                result += nums[i]
        return result
        
# @lc code=end

