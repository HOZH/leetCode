#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_max = 0
        current = 0
        for i in gain:
            current+=i
            current_max = max(current_max,current)
        return current_max
        
# @lc code=end

