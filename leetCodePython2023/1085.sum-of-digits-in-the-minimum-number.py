#
# @lc app=leetcode id=1085 lang=python3
#
# [1085] Sum of Digits in the Minimum Number
#

# @lc code=start
class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        return 0 if (sum(list(map(lambda x: int(x), [*str(min(nums))]))) % 2 != 0) else 1

# @lc code=end
