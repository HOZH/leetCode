#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        length = len(deck)
        pt = length
        lis = deck[:]

        lis.sort()

        deq = deque()

        deq.append(lis[-1])
        pt -= 2

        while pt >= 0:

            temp = deq.pop()

            deq.appendleft(temp)
            deq.appendleft(lis[pt])

            pt -= 1

        return list(deq)
