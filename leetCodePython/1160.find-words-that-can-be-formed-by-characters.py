#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        count = 0
        a = Counter(chars)
        for i in words:

            temp = a.copy()

            adding = True

            for j in i:

                current = temp[j]

                if temp[j] > 0:

                    temp[j] -= 1

                else:

                    adding = False
                    break

            if adding:
                count += len(i)

        return count
