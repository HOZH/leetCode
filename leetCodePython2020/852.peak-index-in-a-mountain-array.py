#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        l, r = 0, len(A)

        while l < r:

            m = l + (r-l)//2

            if A[m] > A[m+1]:
                r = m

            else:
                l = m+1

        return l

# @lc code=end
