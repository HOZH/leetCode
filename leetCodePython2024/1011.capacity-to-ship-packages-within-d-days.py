#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def helper(capacity):
            current_days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    current_days += 1
                    if current_days > days:  # cannot ship within D days
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
