#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(list(map(lambda x: sum(list(map(lambda y: int(y), [*str(x)]))), nums))))

# @lc code=end
