#
# @lc app=leetcode id=1387 lang=python3
#
# [1387] Sort Integers by The Power Value
#

# @lc code=start

from functools import lru_cache
from collections import defaultdict


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        @lru_cache(None)
        def get_power(current: int):

            if current == 1:
                return 0

            else:
                if current % 2 == 0:
                    current = current//2

                else:
                    current = 3*current+1

                return 1+get_power(current)

        powers = defaultdict(list)

        for i in range(lo, hi+1):

            current_power = get_power(i)

            powers[current_power].append(i)

        keys = sorted(list(powers.keys()))

        result = []

        for i in keys:

            result.extend(sorted(powers[i]))

        return result[k-1]

# @lc code=end
