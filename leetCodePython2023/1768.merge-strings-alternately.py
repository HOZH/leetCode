#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        result = ''
        for i in range(min_len):
            result+=word1[i]
            result+=word2[i]
        
        if len(word1)>min_len:
            result+=word1[min_len:]
        elif len(word2)>min_len:
            result+=word2[min_len:]

        return result
        
# @lc code=end

