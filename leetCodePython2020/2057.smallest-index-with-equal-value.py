#
# @lc app=leetcode id=2057 lang=python3
#
# [2057] Smallest Index With Equal Value
#

# @lc code=start
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            current = nums[i]
            if i % 10 == current:
                return i

        return -1

# @lc code=end
