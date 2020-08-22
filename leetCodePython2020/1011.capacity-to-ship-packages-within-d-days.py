#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def helper(w):
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
        result = r

        while l <= r:

            m = l + (r-l)//2

            if helper(m):
                r = m-1
                result = min(m, result)

            else:
                l = m+1

        return result

# @lc code=end
