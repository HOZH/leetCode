#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1
# @lc code=end
