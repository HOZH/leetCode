#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp = sorted(nums)
        return nums == temp or nums == temp[::-1]

# @lc code=end
