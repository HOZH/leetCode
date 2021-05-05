#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
from itertools import product


class Solution:
    def countVowelStrings(self, n: int) -> int:

        # a = map(lambda x:list(x),product(['a', 'e', 'i', 'o', 'u'], repeat=n))
        # b = list(filter(lambda x: x == sorted(x), a))

        # return len(b)
        return ((n + 1) * (n + 2) * (n + 3) * (n + 4)) // 24

        # return sorted(list(filter(,n)))

# @lc code=end
