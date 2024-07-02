#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(list(map(lambda x: int(x), [*(str(num))])))
        return (digits[0]+digits[1])*10+sum(digits[-2:])

# @lc code=end
