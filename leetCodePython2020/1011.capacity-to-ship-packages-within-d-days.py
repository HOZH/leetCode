#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def is_possible(w):
            count = 0
            remaining = w
            for i in weights:
                if count > D:
                    return False
                if i <= remaining:
                    remaining -= i
                else:
                    remaining = w-i
                    count += 1

            return count+1 <= D

        l, r = max(weights), sum(weights)

        while l < r:
            m = l + (r-l)//2
            if is_possible(m):
                r = m
            else:
                l = m+1

        return l

# @lc code=end
