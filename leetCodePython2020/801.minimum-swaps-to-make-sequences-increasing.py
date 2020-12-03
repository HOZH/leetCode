#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#

# @lc code=start
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:

        keep, swap = [9999 for _ in range(len(A))], [9999 for _ in range(len(A))]

        keep[0] = 0
        swap[0] = 1
        for i in range(len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                # no swapping needed
                keep[i] = keep[i-1]
                # swap A[i] and B[i] since A[i-1] and B[i-1] were swapped as well in this case
                swap[i] = swap[i-1]+1
            if B[i] > A[i-1] and A[i] > B[i-1]:
                # A[i-1] and B[i-1] weren't swapped
                swap[i] = min(swap[i], keep[i-1]+1)
                # swapped A[i-1] and B[i-1], no swap needed for A[i] and B[i]
                keep[i] = min(keep[i], swap[i-1])

        return min(keep[-1], swap[-1])


# @lc code=end
