#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:

        memo = defaultdict(int)
        for char in s:
            memo[char] += 1

        count = 0

        for char in t:
            if memo[char]:
                memo[char] -= 1

            else:
                count += 1

        return count


# @lc code=end
