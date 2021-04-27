#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
# √[(X1－X2) ^ 2+(Y1－Y2) ^ 2]
import math


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        return list(map(lambda current: sum(list(map(lambda current_point: 1 if abs(math.sqrt((current[0]-current_point[0])**2+(current[1]-current_point[1])**2)) <= current[2] else 0, points))), queries))

# @lc code=end
