#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        seen = set()
        for val in counter.values():
            if val not in seen:
                seen.add(val)
            else:
                return False
        return True

# @lc code=end
