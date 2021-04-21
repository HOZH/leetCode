#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
from functools import lru_cache
# @lc code=start


class Solution:

    @lru_cache(None)
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n <= 2:
            return 1

        return self.fib(n-1)+self.fib(n-2)


# @lc code=end
