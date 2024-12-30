#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, n: int) -> int:
        if n < 10:
            return n

        n_str = str(n)
        while len(n_str) > 1:
            temp = 0
            for i in n_str:
                temp += int(i)
            n_str = str(temp)

        return int(n_str)

    # def addDigits(self, num: int) -> int:  # 10
    #     return 1 + (num - 1) % 9 if num else 0


# @lc code=end
