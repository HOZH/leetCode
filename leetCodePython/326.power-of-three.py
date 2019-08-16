#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#


class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n < 1:
            return False
        else:

            a = math.log(n, 3)
            

            return abs(a - round(a)) < 0.0000000001
            # # is_integer()
