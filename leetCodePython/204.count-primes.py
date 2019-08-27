#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#


class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2:

            return 0

        is_prime = [True]*n

        for i in range(2, n):

            if is_prime[i]:

                j = 2

                while i*j < n:

                    is_prime[i*j] = False

                    j += 1

        return sum(is_prime)-2
