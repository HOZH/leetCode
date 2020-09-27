#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        starting_cities = set()
        for i, j in paths:
            starting_cities.add(i)

        for i, j in paths:

            if j not in starting_cities:
                return j

        return ''

# @lc code=end
