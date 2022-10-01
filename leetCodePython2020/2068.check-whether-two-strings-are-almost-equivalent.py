#
# @lc app=leetcode id=2068 lang=python3
#
# [2068] Check Whether Two Strings are Almost Equivalent
#

# @lc code=start
from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        c1, c2 = Counter(word1), Counter(word2)
        c1.subtract(c2)

        for freq in c1.values():
            if abs(freq) > 3:
                return False

        return True


# @lc code=end
