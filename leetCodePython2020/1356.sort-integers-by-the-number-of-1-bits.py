#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#

# @lc code=start
from collections import defaultdict


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp = defaultdict(list)
        for i in arr:
            length = (bin(i))[2:].count('1')
            temp[length].append(i)

        keys = list(temp.keys())
        keys.sort()

        res = []

        for i in keys:
            res.extend(sorted(temp[i]))

        return res


# @lc code=end
