#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_sums, right_sums = [0]*length, [0]*length
        for i in range(1,length):
            left_sums[i]= left_sums[i-1]+nums[i-1]
        for i in range(length-2,-1,-1):
            right_sums[i]=right_sums[i+1]+nums[i+1]

        return [ abs(left_sums[i]-right_sums[i])for i in range(len(nums))]
        
# @lc code=end

