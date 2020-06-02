#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#

# @lc code=start
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()

        result = deque()
        index = len(deck)-2
        result.append(deck[-1])

        while index >= 0:
            temp = result.pop()
            result.appendleft(temp)
            result.appendleft(deck[index])
            index -= 1

        return result

# @lc code=end
