#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#

# @lc code=start
from collections import OrderedDict


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        container = OrderedDict()

        for current in arr:
            if current not in container:
                container[current] = 1
            else:
                container[current] += 1

        for key, count in container.items():

            if count == 1:
                k -= 1
            if k == 0:
                return key

        return ''


# @lc code=end
