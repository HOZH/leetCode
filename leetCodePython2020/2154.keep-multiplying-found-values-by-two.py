#
# @lc app=leetcode id=2154 lang=python3
#
# [2154] Keep Multiplying Found Values by Two
#

# @lc code=start
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums, result = set(nums), original
        while result in nums:
            result *= 2
        return result
# @lc code=end
