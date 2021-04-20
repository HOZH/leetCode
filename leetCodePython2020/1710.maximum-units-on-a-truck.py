#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#

# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: x[1], reverse=True)

        ans = 0

        for i in range(len(boxTypes)):

            incoming_loads = min(truckSize, boxTypes[i][0])
            ans += incoming_loads*boxTypes[i][1]

            truckSize -= incoming_loads
            if truckSize <= 0:
                break

        return ans

        # @lc code=end
