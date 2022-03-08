#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s_counter, t_counter = Counter(s), Counter(t)
        t_counter.subtract(s_counter)
        return max(t_counter.items(), key=lambda x: x[1])[0]

# @lc code=end
