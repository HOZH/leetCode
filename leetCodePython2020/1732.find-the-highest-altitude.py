#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        highest = current = 0

        for i in gain:
            current += i
            highest = max(highest, current)

        return highest
# @lc code=end
