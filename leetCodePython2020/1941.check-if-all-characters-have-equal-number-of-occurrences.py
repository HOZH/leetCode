#
# @lc app=leetcode id=1941 lang=python3
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
from collections import defaultdict, Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if not len(s):
            return True
        counter = Counter(s)
        values = list(counter.values())
        temp = values[0]
        return values.count(temp) == len(s)/temp

    def areOccurrencesEqualTemp(self, s: str) -> bool:

        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        temp = -1
        for key in counter.keys():
            if temp == -1:
                temp = counter[key]
                continue
            if counter[key] != temp:
                return False

        return True


# @lc code=end
