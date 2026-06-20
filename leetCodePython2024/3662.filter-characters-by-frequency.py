#
# @lc app=leetcode id=3662 lang=python3
#
# [3662] Filter Characters by Frequency
#

# @lc code=start
from collections import Counter


class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        counter = Counter(s)
        return ''.join([x for x in s if counter[x] < k])

# @lc code=end
