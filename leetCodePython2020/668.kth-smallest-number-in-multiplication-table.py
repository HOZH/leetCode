#
# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#

# @lc code=start

from bisect import bisect


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def LEX(m, n, x, k):
            count = 0
            for i in range(1, min(m + 1, x + 1)):
                count += min(n, x // i)
                if count >= k:
                    return count
            return count
        # matrix = [[0 for _ in range(n)] for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         matrix[i][j] = (i+1)*(j+1)
        # l, r = matrix[0][0], matrix[-1][-1]
        l, r = 1, m*n+1
        while l < r:
            pivot = l + (r-l)//2
            if LEX(m, n, pivot, k) < k:
                l = pivot+1
            else:
                r = pivot

        return l

# @lc code=end
