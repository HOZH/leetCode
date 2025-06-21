#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
from functools import lru_cache


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        dp = [[False] * length for _ in range(length)]
        # single characters are palindromes
        for i in range(length):
            dp[i][i] = True
            count += 1
        # two characters are palindromes if they are equal
        for i in range(length-1):
            dp[i][i+1] = s[i] == s[i+1]
            count += 1 if dp[i][i+1] else 0
        # check for substring length from 3 to length of input string
        for sub_string_length in range(3, length+1):
            for i in range(length-sub_string_length+1):
                j = i + sub_string_length - 1
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                count += 1 if dp[i][j] else 0

        return count

    def countSubstrings_temp(self, s: str) -> int:
        @lru_cache(None)
        def is_palindrome(candidate):
            return candidate == candidate[::-1]
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    count += 1
        return count

# @lc code=end
