#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        return abs(sum(nums)-sum(map(lambda x: sum(map(lambda x: int(x), [*str(x)])), nums)))

# @lc code=end
