#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 4:
            return -1
        return nums[-1]*nums[-2]-nums[0]*nums[1]
# @lc code=end
