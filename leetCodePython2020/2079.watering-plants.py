#
# @lc app=leetcode id=2079 lang=python3
#
# [2079] Watering Plants
#

# @lc code=start
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        current = capacity
        steps = 0

        for i in range(len(plants)):
            if plants[i] <= current:
                current -= plants[i]
                steps += 1
            else:
                steps += 2*i+1
                current = capacity-plants[i]
        return steps

# @lc code=end
