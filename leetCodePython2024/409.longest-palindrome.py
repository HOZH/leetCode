#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        bag = defaultdict(int)
        for i in s:
            bag[i] += 1
        has_odd_count_char = False
        ans = 0
        for value in bag.values():
            if value % 2 == 0:
                ans += value
            else:
                ans += value-1
                has_odd_count_char = True

        if has_odd_count_char:
            ans += 1
        return ans


# @lc code=end
