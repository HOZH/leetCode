#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatAll(speed):
            count = 0
            for i in piles:
                count += math.ceil(i/speed)
                if count > h:
                    return False
            return True

        l, r = 1, max(piles)

        while l < r:
            m = l+(r-l)//2

            if canEatAll(m):
                r = m
            else:
                l = m+1

        return l


# @lc code=end
