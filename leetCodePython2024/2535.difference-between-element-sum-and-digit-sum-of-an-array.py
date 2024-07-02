#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        for i in nums:
            digit_sum += sum(list(map(lambda x: int(x), [*str(i)])))

        return abs(digit_sum - sum(nums))

# @lc code=end
