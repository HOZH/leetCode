#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, sum(piles)

        def helper(eating_speed):
            hours = 0
            for i in piles:
                if i <= eating_speed:
                    hours += 1
                else:
                    hours += ceil(i/eating_speed)
                if hours > h:
                    return False
            return True

        while left < right:
            mid = left+(right-left)//2
            if helper(mid):
                right = mid
            else:
                left = mid+1

        return left


# @lc code=end
