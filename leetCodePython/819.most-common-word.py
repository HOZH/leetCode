#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # gonna redo this question after I reviewed regular ex
        temp = paragraph.casefold().replace(',', ' ', -1).replace(';', ' ', -1).replace('\'', ' ', -1).replace('?', ' ', -1).replace('.',
                                                                                                                                     ' ', -1).replace('!', ' ', -1).split()

        temp = list(filter(lambda x: x not in banned, temp))

        print(temp)

        print(Counter(temp))

        return max(temp, key=temp.count)
