#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:

        origin = A

        count = 1

        while len(A) <= 2*len(B) or count < 5:

            if A.__contains__(B):
                return count

            A += origin
            count += 1

        return -1
