#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
from collections import defaultdict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        cities = defaultdict(int)

        for i, j in paths:
            cities[i] += 1
            cities[j] -= 1

        for i, j in cities.items():
            if j == -1:
                return i


# @lc code=end
