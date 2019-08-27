#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#


from math import *


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        if c == 0 or c == 1:
            return True

        for i in range(1, c):

            current = i**2

            if current <= c:

                if sqrt(c-current).is_integer():

                    return True

            else:
                break

        return False
