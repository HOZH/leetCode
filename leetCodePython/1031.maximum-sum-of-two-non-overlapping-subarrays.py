#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:

        def helper(a, l, m):
            first, sec = l, m

            length = len(A)

            max_first, max_sec = -1, -1

            f = -1

            for i in range(length - first):
                current = sum(A[i:i + first])
                if current > max_first:
                    f = i
                    max_first = current

            if f > sec:
                for i in range(f - sec):

                    current = sum(A[i:i + sec])
                    if current > max_sec:
                        s = i
                        max_sec = current

            for i in range(f + first, length - sec+1):

                current = sum(A[i:i + sec])
                if current > max_sec:
                    max_sec = current

            return max_first + max_sec

        return max(helper(A, M, L), helper(A, L, M))
