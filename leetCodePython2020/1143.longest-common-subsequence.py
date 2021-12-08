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
        def helper(str1, str2):
            if not len(str1) or not len(str2):
                return 0

            letter1 = str1[0]
            first_letter1_in_str2 = str2.find(letter1)

            remain_str1 = str1[1:]
            if first_letter1_in_str2 == -1:
                return helper(remain_str1, str2)

            # case 1, first letter not included in the optimal result
            case1 = helper(remain_str1, str2)
            # case 2, first letter is in the optimal result
            case2 = 1 + helper(remain_str1, str2[first_letter1_in_str2+1:])

            return max(case1, case2)

        return helper(text1, text2)


# @lc code=end
