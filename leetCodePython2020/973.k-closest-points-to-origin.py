#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from heapq import nsmallest
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return nsmallest(K, points, key=lambda x: sqrt(x[0]**2+x[1]**2))


# @lc code=end
