#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def lcs(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # case1 = lcs(p1+1, p2)
            # letter1 = text1[p1]
            # first_occurence = text2.find(letter1, p2)

            # case2 = 0
            # if first_occurence != -1:
            #     case2 = 1 + lcs(p1+1, first_occurence+1)
            if text1[p1] == text2[p2]:
                return 1 + lcs(p1 + 1, p2 + 1)
            else:
                return max(lcs(p1 + 1, p2), lcs(p1, p2 + 1))

            # return max(case1, case2)
        return lcs(0, 0)


# @lc code=end
