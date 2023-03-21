#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len(list(filter(lambda x: x < 0, nums))), len(list(filter(lambda x: x > 0, nums))))

# @lc code=end
