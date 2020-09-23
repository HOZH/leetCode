#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start


class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):

                if s[i] != s[j]:
                    continue

                sub = s[i:j+1]
                if sub == sub[::-1]:
                    count += 1

        return count

# @lc code=end
