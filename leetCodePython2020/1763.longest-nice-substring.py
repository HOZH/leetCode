#
# @lc app=leetcode id=1763 lang=python3
#
# [1763] Longest Nice Substring
#

# @lc code=start
from functools import lru_cache


class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        @lru_cache(None)
        def helper(string):

            lower, upper = set(), set()

            for i in string:

                if 65 <= ord(i) <= 90:

                    upper.add(chr(ord(i)+32))

                else:
                    lower.add(i)

            return len(string) if lower == upper else -1

        max_len = -1
        first_occurence = ''
        for i in range(len(s)):

            for j in range(len(s)+1, i, -1):

                temp = helper(s[i:j])

                if temp > max_len:
                    max_len = temp
                    first_occurence = s[i:j]
                    break

        return first_occurence


# @lc code=end
