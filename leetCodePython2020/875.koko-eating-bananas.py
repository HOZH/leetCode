#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(K):
            return sum((p-1)//K + 1 for p in piles) <= H

        l, r = 1, max(piles)
        if H == len(piles):
            return r
        while l < r:
            m = l + (r-l)//2
            if possible(m):
                r = m
            else:
                l = m + 1
        return l


# @lc code=end
