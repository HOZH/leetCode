#
# @lc app=leetcode id=3925 lang=python3
#
# [3925] Concatenate Array With Reverse
#

# @lc code=start
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums+nums[::-1]

# @lc code=end
