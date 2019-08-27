#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        counter = collections.Counter(deck)

        min_count = min(counter.items(), key=lambda x: x[1])[1]

        if min_count < 2:

            return False

        for i in range(min_count, 1, -1):

            if min_count % i == 0:

                if all(counter[x] % i == 0 for x in counter):
                    return True

        return False
