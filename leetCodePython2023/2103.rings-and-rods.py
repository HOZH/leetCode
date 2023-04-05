#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(set)

        for i in range(0, len(rings), 2):
            rods[rings[i+1]].add(rings[i])
            print(rings[i+1], rings[i])

        return len(list(filter(lambda x: len(x) > 2, list(rods.values()))))


# @lc code=end
