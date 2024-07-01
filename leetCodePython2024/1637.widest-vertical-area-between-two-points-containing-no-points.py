#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        current_max = 0
        for i in range(1,len(points)):
            current_max = max(current_max,points[i][0]-points[i-1][0])

        return current_max
        
# @lc code=end

