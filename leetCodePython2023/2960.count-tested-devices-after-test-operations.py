#
# @lc app=leetcode id=2960 lang=python3
#
# [2960] Count Tested Devices After Test Operations
#

# @lc code=start
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:

        count = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                count += 1
                for j in range(i+1, len(batteryPercentages)):
                    batteryPercentages[j] -= 1
                    batteryPercentages[j] = max(0, batteryPercentages[j])

        return count


# @lc code=end
