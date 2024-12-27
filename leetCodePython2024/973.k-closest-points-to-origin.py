#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def get_euclidean_distance(point):
            x, y = point
            return sqrt(x**2 + y**2)

        points.sort(key=get_euclidean_distance)
        return points[:k]

# @lc code=end
