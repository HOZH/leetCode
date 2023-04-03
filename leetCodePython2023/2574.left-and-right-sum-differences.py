#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_sums = [0]*length
        right_sums = [0]*length
        ans = []

        for i in range(1, length):
            left_sums[i] = left_sums[i-1]+nums[i-1]
        for i in range(length-2, -1, -1):
            right_sums[i] = right_sums[i+1]+nums[i+1]

        for i in range(length):
            ans.append(abs(left_sums[i]-right_sums[i]))

        return ans


# @lc code=end
