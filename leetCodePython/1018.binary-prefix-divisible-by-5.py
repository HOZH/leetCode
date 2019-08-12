#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:

        current = 0

        for i in range(len(A)):

            current <<= 1
            current += A[i]

            A[i] = (current % 5 == 0)

        return A
