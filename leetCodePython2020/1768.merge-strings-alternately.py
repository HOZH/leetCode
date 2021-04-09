#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        shorter_len = min(len(word1), len(word2))
        diff = abs(len(word1)-len(word2))

        ans = ''

        for i in range(shorter_len):
            ans += word1[i]
            ans += word2[i]

        if len(word1) < len(word2):

            ans += word2[-diff:]

        elif len(word1) > len(word2):

            ans += word1[-diff:]

        return ans


# @lc code=end
