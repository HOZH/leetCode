#
# @lc app=leetcode id=2083 lang=python3
#
# [2083] Substrings That Begin and End With the Same Letter
#

# @lc code=start
from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        for i in counter.values():
            ans += (1+i)*i//2
        return ans


# @lc code=end
