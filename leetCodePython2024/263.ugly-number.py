#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def __init__(self):
        self.allowed_primes = set([2, 3, 5])

    def isUgly(self, n: int) -> bool:

        if n < 1:
            return False
        if n == 1:
            return True

        if n in self.allowed_primes:
            return True

        failure_count = 0
        for i in self.allowed_primes:
            if n % i == 0 and self.isUgly(n // i):
                return True

            failure_count += 1
            if failure_count == 3:
                return False


# @lc code=end
