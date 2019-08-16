#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n < 1:
            return False
        else:

            a = math.log(n, 2)
            return abs(a - int(a)) < 0.0000000001
        # is_integer()


    
