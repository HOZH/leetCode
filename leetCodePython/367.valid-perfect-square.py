#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#


class Solution:

    def isPerfectSquare(self, num: int) -> bool:

        # could use binary search to establish upper/lower bound for i to achieve a better performance

        upper = 10**10  # big enough for the testcases

        lower = 0

        pivot = (upper+lower)//2

        while upper >= lower:

            current = pivot ** 2
            if current == num:

                return True

            elif current < num:

                lower = pivot+1

            else:

                upper = pivot-1

            pivot = (upper+lower)//2

        return False
