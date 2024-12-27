#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1, len_word2 = len(word1), len(word2)
        self.ans = ''
        for i in range(min(len_word1, len_word2)):
            self.ans += word1[i]+word2[i]

        if len_word1 == len_word2:
            return self.ans
        elif len_word1 > len_word2:
            self.ans += word1[len_word2:]
        else:
            self.ans += word2[len_word1:]

        return self.ans

# @lc code=end
