#
# @lc app=leetcode id=1837 lang=python3
#
# [1837] Sum of Digits in Base K
#

# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:

        digit = 0
        sum = 0
        while n > 0:
            digit = n % k
            sum += digit
            n //= k

        return sum

# @lc code=end
