#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

from collections import deque


class Solution:
    def rotateString(self, A: str, B: str) -> bool:

        if A == '' and B == '':
            return True

        a = deque(A)

        b = deque(i for i in B)

        for i in range(len(a)):

            a.rotate(1)

            if a == b:

                return True

        return False
