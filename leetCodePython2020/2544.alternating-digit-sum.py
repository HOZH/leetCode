#
# @lc app=leetcode id=2544 lang=python3
#
# [2544] Alternating Digit Sum
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        n = str(n)
        is_positive = True
        for i in n:
            if is_positive:
                ans += int(i)
            else:
                ans -= int(i)
            is_positive = not is_positive
        return ans

# @lc code=end
