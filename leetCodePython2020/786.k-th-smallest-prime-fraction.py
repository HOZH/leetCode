#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start


class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:

        n = len(A)
        l, r = 0, 1
        while l < r:
            m = (l+r)/2
            max_f = 0
            # how many elements smaller than m
            total = 0
            # the row,col index of the max_f
            # p, q = 0, 0
            j = 1

            for i in range(n-1):
                # while j < n and A[i] > m*A[j]:
                while j < n and A[i]/A[j] > m:
                    j += 1

                if j == n:
                    break

                # n-j -> how many in current row < m
                total += n-j

                f = A[i]/A[j]
                if f > max_f:
                    p, q, max_f = i, j, f

            if total == K:
                return [A[p], A[q]]
            elif total > K:
                r = m
            else:
                l = m
        return []

# @lc code=end
