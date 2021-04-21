#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:

        current_base = 0
        current = 1
        ans = 0

        for i in range(1, n+1):

            if i % 7 == 1:
                current_base += 1
                current = current_base
            else:
                current += 1

            ans += current

        return ans


# @lc code=end
