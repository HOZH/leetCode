#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(list(map(lambda x: len(x.split(' ')), sentences)))

# @lc code=end
