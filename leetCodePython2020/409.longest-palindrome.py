#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:

        counter = Counter(s)
        ans = 0
        for i in counter.values():
            ans += i//2
        ans *= 2
        if ans < len(s):
            ans += 1
        return ans

# @lc code=end
