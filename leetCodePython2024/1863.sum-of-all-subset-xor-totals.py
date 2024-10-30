#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
from functools import reduce
import itertools


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        def powerset(iterable):
            s = list(iterable)
            return itertools.chain.from_iterable(
                itertools.combinations(s, r) for r in range(len(s)+1)
            )
        powerset = list(filter(lambda x: len(x) != 0, powerset(nums)))
        ans = 0
        for i in powerset:
            ans += reduce(lambda x, y: x ^ y, i)

        return ans


# @lc code=end
