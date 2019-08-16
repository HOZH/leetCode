#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#


class Solution:
    def isPowerOfFour(self, num: int) -> bool:

        if num < 1:
            return False
        else:

            a = math.log(num, 4)

            return abs(a - round(a)) < 0.0000000001
            # # is_integer()
