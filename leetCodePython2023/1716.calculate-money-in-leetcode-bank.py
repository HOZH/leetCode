#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:

        weeks = n//7
        days = n % 7
        result = 0
        # 28 = (1+2+3+4+5+6+7)
        if weeks > 0:
            result += weeks*28
            result += (weeks*(weeks-1))//2*7

        for i in range(1, days+1):
            result += weeks+i

        return result


# @lc code=end
