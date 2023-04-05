#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        words = list(map(lambda x: x[-1]+x[:-1], s.split(' ')))
        words.sort()

        return " ".join(list(map(lambda x: x[1:], words)))


# @lc code=end
