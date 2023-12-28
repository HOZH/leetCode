#
# @lc app=leetcode id=1941 lang=python3
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        prev_count = None
        for i in c.values():
            if prev_count == None:
                prev_count = i
            else:
                if i != prev_count:
                    return False
        return True

# @lc code=end
