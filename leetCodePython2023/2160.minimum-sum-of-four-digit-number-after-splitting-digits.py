#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted([*str(num)], reverse=True)
        num1 = num2 = 0
        for _ in range(2):
            num1 = 10*num1+int(digits.pop())
            num2 = 10*num2+int(digits.pop())

        return num1+num2


# @lc code=end
