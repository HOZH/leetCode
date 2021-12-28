#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return len(max(sentences, key=lambda x: len(x.split(' '))).split(' '))

# @lc code=end
