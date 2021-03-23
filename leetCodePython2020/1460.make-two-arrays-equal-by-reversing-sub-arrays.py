#
# @lc app=leetcode id=1460 lang=python3
#
# [1460] Make Two Arrays Equal by Reversing Sub-arrays
#

# @lc code=start
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        a, b = Counter(target), Counter(arr)

        return a.items() == b.items()


# @lc code=end
