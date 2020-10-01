#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        for p in "!?',;.":

            paragraph = paragraph.replace(p, ' ')

        paragraph = paragraph.lower().split()

        dic = defaultdict(int)

        for i in paragraph:
            if i not in banned:
                dic[i] += 1

        return max(dic, key=dic.get)


# @lc code=end
