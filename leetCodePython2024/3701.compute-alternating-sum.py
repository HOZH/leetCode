#
# @lc app=leetcode id=3701 lang=python3
#
# [3701] Compute Alternating Sum
#

# @lc code=start
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 2 != 0:
                nums[i] = -nums[i]
        return sum(nums)

# @lc code=end
