#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start
from collections import defaultdict, Counter
import math
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:


        A.sort()
        n = len(A)

        l, r = 0, A[-1]-A[0]

        while l <= r:
            count = 0

            j = 0

            m = l + (r-l)//2

            for i in range(n):
                while (j < n and A[j]-A[i] <= m):
                    # increase j until A[j] - A[i] >m
                    j += 1
                # not zeroed out => count = previous count+ j-i-1
                count += j - i - 1

            if count >= K:
                r = m-1
            else:
                l = m+1
        return l
        
# @lc code=end

