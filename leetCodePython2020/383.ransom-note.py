#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s_counter, t_counter = Counter(ransomNote), Counter(magazine)
        t_counter.subtract(s_counter)
        return all(map(lambda x: x[1] >= 0, t_counter.items()))

# @lc code=end
