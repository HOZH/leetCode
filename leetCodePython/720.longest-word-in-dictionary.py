#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#


class Solution:
    def longestWord(self, words):

        #getting familiar about all()
    
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word

        return ans
