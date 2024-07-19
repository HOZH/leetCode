#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height, current_height = 0, 0
        for i in gain:
            current_height += i
            max_height = max(max_height, current_height)

        return max_height

# @lc code=end
