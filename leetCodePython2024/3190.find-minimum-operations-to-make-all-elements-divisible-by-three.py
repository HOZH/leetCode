#
# @lc app=leetcode id=3190 lang=python3
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for i in nums if i % 3 != 0)

# @lc code=end
