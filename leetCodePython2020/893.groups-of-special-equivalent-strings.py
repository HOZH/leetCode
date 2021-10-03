#
# @lc app=leetcode id=893 lang=python3
#
# [893] Groups of Special-Equivalent Strings
#

# @lc code=start

from collections import Counter


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:

        if not len(words):
            return 0

        result = set()

        for w in words:

            current = ''.join(sorted(w[1::2])+sorted(w[::2]))
            result.add(current)

        return len(result)

# @lc code=end
