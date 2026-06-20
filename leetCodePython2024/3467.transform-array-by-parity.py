#
# @lc app=leetcode id=3467 lang=python3
#
# [3467] Transform Array by Parity
#

# @lc code=start
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        even_count = len(list(filter(lambda x: x % 2 == 0, nums)))
        return [0]*even_count+[1]*(length-even_count)

# @lc code=end
