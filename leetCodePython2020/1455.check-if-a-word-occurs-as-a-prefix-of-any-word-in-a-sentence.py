#
# @lc app=leetcode id=1455 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lis = sentence.split(' ')
        for i in range(len(lis)):
            if lis[i].startswith(searchWord):
                return i+1
                
        return -1
        
# @lc code=end

