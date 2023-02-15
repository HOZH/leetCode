#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#

# @lc code=start
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:

        # keep[i] = number of swaps is needed when ith is not swapped (must)
        # swap[i] = number of swaps is needed when ith is swapped (must)
        keep, swap = [100001 for _ in range(len(A))], [
            100001 for _ in range(len(A))]

        keep[0] = 0
        swap[0] = 1  # swap once when the length of arrays are 1 -> it's valid

        for i in range(1, len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                # no swapping needed, so swaps need for keep[i] = keep[i-1] ->
                # i-1 and i are both not swapped
                keep[i] = keep[i-1]
                # both i and i-1 are swapped
                # swap A[i] and B[i] since A[i-1] and B[i-1] were swapped as well in this case
                swap[i] = swap[i-1]+1
            if B[i] > A[i-1] and A[i] > B[i-1]:
                # i-1 didn't swap, now swap i -> keep[i-1]+1

                # or use swap[i] (swap[i-1]+1 from previous condition) -> only valid
                # if B[i] > A[i-1] and A[i] > B[i-1] else swap[i] = 100001
                # so swap ith to match -> i-1 already swapped so swap i as well

                # swap[i] seems useless, but it only valid when previous condition is also valid
                # else swap[i] = 100001
                # that means swap[i] = swap[i-1]+1
                # so it could provide us a better result if swap[i-1] < keep[i-1]
                # that's possible, and that's the only use case
                # this logic bugged me for like 30 mins, fuck it
                swap[i] = min(keep[i-1]+1, swap[i])

                # swapped A[i-1] and B[i-1], no swap needed for A[i] and B[i] -> swap[i-1]

                # also if A[i] > A[i-1] and B[i] > B[i-1]
                # then use min value from keep[i]-> keep[i] = keep[i-1]
                # both i and i-1 not swapped

                keep[i] = min(swap[i-1], keep[i])

        return min(keep[-1], swap[-1])


# @lc code=end
