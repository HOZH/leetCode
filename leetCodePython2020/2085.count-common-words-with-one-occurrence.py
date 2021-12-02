#
# @lc app=leetcode id=2085 lang=python3
#
# [2085] Count Common Words With One Occurrence
#

# @lc code=start
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        set1, set2 = set(words1), set(words2)
        words1 = set(filter(lambda x: words1.count(x) == 1, words1))
        words2 = set(filter(lambda x: words2.count(x) == 1, words2))

        return len(words1 & words2)


# @lc code=end
