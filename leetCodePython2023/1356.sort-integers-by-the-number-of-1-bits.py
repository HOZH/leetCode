#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#

# @lc code=start
from collections import defaultdict


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        bit_dict = defaultdict(list)

        for i in arr:
            temp = "{0:b}".format(i)
            bit_dict[temp.count('1')].append(i)

        bit_keys = list(bit_dict.keys())
        bit_keys.sort()

        ans = []
        for key in bit_keys:
            ans.extend(sorted(bit_dict[key]))

        return ans


# @lc code=end
