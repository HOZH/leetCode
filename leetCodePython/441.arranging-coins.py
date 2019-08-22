#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#


class Solution:
    def arrangeCoins(self, n: int) -> int:

        # could use binary search method instead and formual n*(n-1)/2

        current = 1

        result = 0

        while True:

            result += current

            if result > n:

                return current-1
            current += 1
