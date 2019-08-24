#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        length = len(A)

        if length < 3:
            return False

        peak = False

        prev = A[0]

        first = True

        first_half = False

        for i in range(1, length):

            if prev == A[i]:
                return False

            elif prev < A[i]:

                first_half = True

                if peak:
                    return False

            if prev > A[i]:

                if first:
                    peak = True
                    prev = A[i]
                    first = False

                    continue

                if not peak:
                    return False

            prev = A[i]

        return True if (peak and first_half) else False
