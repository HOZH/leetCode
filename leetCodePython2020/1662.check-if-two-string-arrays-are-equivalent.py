#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
from functools import reduce


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        return reduce(lambda a, b: a+b, word1) == reduce(lambda a, b: a+b, word2)


# @lc code=end
