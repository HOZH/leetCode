#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        temp = []
        for i in range(len(points)):
            current_x, current_y = points[i][0], points[i][1]
            if current_x == x or current_y == y:
                temp.append([current_x, current_y, i])
        temp.sort(key=lambda c: abs(c[0]-x)+abs(c[1]-y))
        return temp[0][2] if len(temp) else -1

# @lc code=end
