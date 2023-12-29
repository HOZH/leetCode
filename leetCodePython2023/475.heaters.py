#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
from bisect import bisect_left


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        new_houses = []
        heater_set = set(heaters)
        for i in houses:
            if i not in heater_set:
                new_houses.append(i)

        min_radius = 0
        for h in new_houses:
            position = bisect_left(heaters, h)
            left, right = position-1, position
            left_heater, right_heater = heaters[left] if (
                left > -1) else float('inf'), heaters[right] if (right < len(heater_set)) else float('inf')

            t1 = min(abs(h-left_heater),
                     abs(h-right_heater))

            min_radius = max(min_radius, t1)

        return min_radius


# @lc code=end
