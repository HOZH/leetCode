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
        for origin, destination in paths:
            cities[origin] += 1
            cities[destination] -= 1

        for city, value in cities.items():
            if value == -1:
                return city
        # guaranteed to have dest city, no final return needed here


# @lc code=end
 loc_dict = {}
        for cities in paths:
            origin = cities[0]
            dest = cities[1]
            if origin in loc_dict:
                loc_dict[origin] += 1
            else:
                loc_dict[origin] = 1
            if dest in loc_dict:
                loc_dict[dest] -= 1
            else:
                loc_dict[dest] = -1

        for city, value in loc_dict.items():
            if value == -1:
                return city