#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#


class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0

        for i in range(1, 17):

            count += n//(5**i)

        return count
